import csv
from django.http import Http404, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from lead.models import Lead , LeadNote
from .filters import ClientFilter
from .serializers import ClientSerializer, NoteSerializer
from .models import Client, Note
from team.models import Team
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from django.db.models import Value
from django.db.models.functions import Concat



class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    parser_classes = (MultiPartParser,FormParser,JSONParser)

    #Filters
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientFilter


    def get_queryset(self):
        team = Team.objects.filter(members__in= [self.request.user]).first()

        return self.queryset.filter(team=team).select_related('created_by','team','address','assigned_to__userprofile')

    #TODO Verificam daca clientul mai exista si daca da nu il mai cream

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        serializer.save(team = team,created_by=self.request.user)

    #detail=False -> actions on the colection not an individual id
    @action(detail=False, methods=['get'], url_path='exportCSV')
    def export_csv(self,request):
        team = Team.objects.filter(members__in=[request.user]).first()
        queryset = Client.objects.filter(team=team).annotate(
            created_by_fullname = Concat('created_by__last_name', Value(' '), 'created_by__first_name')
        ).values(
            'id','name','contact_person','email','phone','status','created_at','created_by_fullname'
        )

        fieldnames= ['id','name','contact_person','email','phone','status','created_at','created_by_fullname']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="leads.csv"'
        response['Access-Control-Expose-Headers'] = 'Content-Disposition'

        writer = csv.DictWriter(response,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(queryset)

        return response





class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in= [self.request.user]).first()
        client_id = self.request.GET.get('client_id')

        return self.queryset.filter(team=team).filter(client_id=client_id)


    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client_id']

        serializer.save(team=team, created_by=self.request.user, client_id=client_id)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def convert_lead_to_client(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data.get('lead_id')

    if not lead_id:
        return Response({"error":'Lead id is missing from the request'},status=400)

    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
        leadNote = LeadNote.objects.filter(team=team,lead=lead)
    except Lead.DoesNotExist:
        raise Http404


    client = Client.objects.create(team=team, name = lead.company, contact_person = lead.contact_person ,
                                   email = lead.email, phone = lead.phone , website = lead.website ,
                                   created_by = request.user, assigned_to=request.user,
                                   last_contacted_date=lead.last_contacted_date, address=lead.address,
                                   source=lead.source)
    if leadNote:
        for item in leadNote:
            client_note = Note.objects.create(team=team,client=client,name=item.name,body=item.body,
                                              created_by=item.created_by,
                                             )



    return Response()











