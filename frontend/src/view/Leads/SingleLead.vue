<template>
  <div v-if="leadStore.lead && !leadStore.loading" class="max-w-6xl mx-auto pb-20">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
      <div class="flex items-center gap-3 bg-white p-2 rounded-xl border border-gray-200 shadow-sm">
        <button
          @click="toggleCheklist"
          class="px-4 py-2 text-sm font-bold text-gray-500 hover:bg-gray-700 hover:text-white rounded-lg transition-all"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M6.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM12.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM18.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"
            />
          </svg>
        </button>
        <div class="w-px h-6 bg-gray-200"></div>
        <button
          @click="toggleModal"
          class="px-4 py-2 text-sm font-bold text-red-300 hover:bg-red-600 hover:text-white rounded-lg transition-all"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M2.25 13.5h3.86a2.25 2.25 0 0 1 2.012 1.244l.256.512a2.25 2.25 0 0 0 2.013 1.244h3.218a2.25 2.25 0 0 0 2.013-1.244l.256-.512a2.25 2.25 0 0 1 2.013-1.244h3.859m-19.5.338V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 0 0-2.15-1.588H6.911a2.25 2.25 0 0 0-2.15 1.588L2.35 13.177a2.25 2.25 0 0 0-.1.661Z"
            />
          </svg>
        </button>
        <div class="w-px h-6 bg-gray-200"></div>
        <button
          @click="handleConvert"
          class="px-4 py-2 text-sm font-bold text-blue-600 hover:bg-blue-600 hover:text-white rounded-lg transition-all"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M18 7.5v3m0 0v3m0-3h3m-3 0h-3m-2.25-4.125a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0ZM3 19.235v-.11a6.375 6.375 0 0 1 12.75 0v.109A12.318 12.318 0 0 1 9.374 21c-2.331 0-4.512-.645-6.374-1.766Z"
            />
          </svg>
        </button>
        <div class="w-px h-6 bg-gray-200"></div>
        <router-link
          :to="{ name: 'EditLead', params: { id: route.params.id } }"
          class="px-4 py-2 text-sm font-bold text-gray-600 hover:bg-gray-600 hover:text-white rounded-lg transition-all"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125"
            />
          </svg>
        </router-link>
        <div class="w-px h-6 bg-gray-200"></div>
        <button
          @click="handleDelete"
          class="px-4 py-2 text-sm font-bold text-red-600 hover:bg-red-600 hover:text-white rounded-lg transition-all"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
            />
          </svg>
        </button>
      </div>
    </div>

    <div v-show="showChecklist">
      <div v-if="lead.status === 'new'" class="my-3">
        <form @submit.prevent="submitChecklist">
          <div
            class="flex items-center ps-4 bg-neutral-primary-soft border border-default rounded-base shadow-xs p-3 mb-3"
          >
            <ul>
              <li>
                <input
                  type="checkbox"
                  id="contacted"
                  name="contacted"
                  v-model="checklist_data.new.contacted"
                  class="w-4 h-4 border border-default-medium rounded-xs bg-neutral-secondary-medium focus:ring-2 focus:ring-brand-soft"
                />
                <label for="contacted" class="text-heading"> Contacted</label>
              </li>
              <li>
                <label for="contact_method">Contact method: </label>
                <select v-model="checklist_data.new.contact_method" class="bg-blue-50 rounded">
                  <option selected disabled class="font-medium">Chose a contact method</option>
                  <option
                    v-for="option in contactMethods"
                    :key="option.value"
                    :value="option.value"
                    class="font-medium"
                  >
                    {{ option.label }}
                  </option>
                </select>
              </li>
            </ul>
          </div>
          <button
            type="submit"
            class="bg-blue-600 hover:bg-white hover:text-blue-600 hover:outline-1 text-white px-4 py-2 rounded font-medium text-sm transition-all disabled:opacity-50"
          >
            Save
          </button>
        </form>
      </div>

      <div v-if="lead.status === 'contacted'" class="my-3 bg-white p-4 rounded shadow">
        <form @submit.prevent="submitChecklist">
          <ul>
            <li>
              <label for="has_budget"> Has Budget </label>
              <input
                type="checkbox"
                id="has_budget"
                name="has_budget"
                v-model="checklist_data.contacted.has_budget"
              />
            </li>
            <li>
              <label for="can_solve_problem"> Can solve problem </label>
              <input
                type="checkbox"
                id="can_solve_problem"
                name="can_solve_problem"
                v-model="checklist_data.contacted.can_solve_problem"
              />
            </li>
            <li>
              <label for="is_decision_maker"> Is decision maker </label>
              <input
                type="checkbox"
                id="is_decision_maker"
                name="is_decision_maker"
                v-model="checklist_data.contacted.is_decision_maker"
              />
            </li>
          </ul>
          <button
            type="submit"
            class="bg-blue-600 hover:bg-white hover:text-blue-600 hover:outline-1 text-white px-4 py-2 mt-2 rounded font-medium text-sm transition-all disabled:opacity-50"
          >
            Save
          </button>
        </form>
      </div>

      <div v-if="lead.status === 'inprogress'" class="my-3 bg-white p-4 rounded shadow">
        <form @submit.prevent="submitChecklist">
          <ul>
            <li>
              <label for="offer_send"> Offer send </label>
              <input
                type="checkbox"
                id="offer_send"
                name="offer_send"
                v-model="checklist_data.inprogress.offer_send"
              />
            </li>
            <li>
              <label for="offer_dicussed"> Offer discussed </label>
              <input
                type="checkbox"
                id="offer_dicussed"
                name="offer_discussed"
                v-model="checklist_data.inprogress.offer_discussed"
              />
            </li>
            <li>
              <label for="negotiation_started"> Negotiation started </label>
              <input
                type="checkbox"
                id="negotiation_started"
                name="negotiation_started"
                value="false"
                v-model="checklist_data.inprogress.negotiation_started"
              />
            </li>
          </ul>
          <button
            type="submit"
            class="bg-blue-600 hover:bg-white hover:text-blue-600 hover:outline-1 text-white px-4 py-2 mt-2 rounded font-medium text-sm transition-all disabled:opacity-50"
          >
            Save
          </button>
        </form>
      </div>
    </div>

    <div class="flex gap-6">
      <div class="bg-white border border-gray-200 shadow-md rounded-2xl p-6 md:p-8 w-2/3">
        <h2 class="text-xl font-bold text-gray-800 mb-6 border-b border-gray-100 pb-4">
          <span class="text-blue-900">{{ lead.company }}</span>
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-6 gap-x-8">
          <div>
            <span class="block text-sm font-medium text-gray-500 mb-1">Contact person</span>
            <span class="block text-base font-semibold text-gray-900">{{
              lead.contact_person || '-'
            }}</span>
          </div>

          <div>
            <span class="block text-sm font-medium text-gray-500 mb-1">Email</span>
            <a
              :href="`mailto:${lead.email}`"
              class="block text-base font-semibold text-blue-600 hover:underline"
            >
              {{ lead.email || '-' }}
            </a>
          </div>

          <div>
            <span class="block text-sm font-medium text-gray-500 mb-1">Phone</span>
            <span class="block text-base font-semibold text-gray-900">{{ lead.phone || '-' }}</span>
          </div>

          <div>
            <span class="block text-sm font-medium text-gray-500 mb-1">Website</span>
            <a
              v-if="lead.website"
              :href="lead.website"
              target="_blank"
              class="block text-base font-semibold text-blue-600 hover:underline"
            >
              {{ lead.website }}
            </a>
            <span v-else class="block text-base font-semibold text-gray-900">N/A</span>
          </div>

          <div>
            <span class="block text-sm font-medium text-gray-500 mb-1">Estimated value</span>
            <span
              class="inline-block px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm font-bold"
            >
              $ {{ lead.estimated_value || '0' }}
            </span>
          </div>

          <div>
            <span class="block text-sm font-medium text-gray-500 mb-1">Confidence</span>
            <span class="block text-base font-semibold text-gray-900"
              >{{ lead.confidence || '0' }} %</span
            >
          </div>

          <div>
            <span class="block text-sm font-medium text-gray-500 mb-1">Status</span>
            <span
              :class="getStatusColor(lead.status)"
              class="inline-flex items-center gap-1.5 px-3 py-1 border rounded-lg text-sm font-bold capitalize transition-colors"
            >
              {{ lead.status }}
            </span>
          </div>

          <div>
            <span class="block text-sm font-medium text-gray-500 mb-1">Priority</span>
            <span class="block text-base font-semibold text-gray-900 capitalize">{{
              lead.priority
            }}</span>
          </div>

          <div>
            <span class="block text-sm font-medium text-gray-500 mb-1">Assigned to</span>
            <span class="block text-base font-semibold text-gray-900">
              {{ lead.assigned_to?.first_name || 'N/A' }} {{ lead.assigned_to?.last_name || '' }}
            </span>
          </div>
        </div>
        <div class="mt-4">
          <button @click="toggleMoreDetails" class="flex items-center gap-1 cursor-pointer">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <polyline points="6 9 12 15 18 9" />
            </svg>
            <span>Show more</span>
          </button>
        </div>
        <div class="mt-4" v-if="showMoreDetails">
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div>
              <span class="block text-sm font-medium text-gray-500 mb-1">Source</span>
              <span class="block text-base font-semibold text-gray-900">
                {{ lead.source ?? 'N/A' }}
              </span>
            </div>

            <div>
              <span class="block text-sm font-medium text-gray-500 mb-1">Next follow up date</span>

              <!-- Mod display: data + buton edit -->
              <div v-if="!editFollowUpDate" class="flex items-center gap-2 group">
                <span class="text-sm font-medium text-gray-900">
                  {{ formatDate(lead.next_follow_up_date) || '—' }}
                </span>
                <button
                  @click="toggleEditFollowUpDate"
                  class="p-1 rounded text-gray-400 hover:text-blue-600 hover:bg-blue-50 transition opacity-0 group-hover:opacity-100"
                  title="Edit date"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" class="w-4 h-4">
                    <path
                      fill="currentColor"
                      d="M1 4c0-1.1.9-2 2-2h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V4zm2 2v12h14V6H3zm2-6h2v2H5V0zm8 0h2v2h-2V0zM5 9h2v2H5V9zm0 4h2v2H5v-2zm4-4h2v2H9V9zm0 4h2v2H9v-2zm4-4h2v2h-2V9zm0 4h2v2h-2v-2z"
                    />
                  </svg>
                </button>
              </div>

              <!--  input + cancel -->
              <div v-else class="flex items-center gap-2">
                <input
                  type="date"
                  v-model="next_follow_up_date"
                  @change="updateFollowUpDate"
                  class="text-sm px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent cursor-pointer"
                />
                <button
                  @click="toggleEditFollowUpDate"
                  class="text-xs text-gray-500 hover:text-gray-700"
                >
                  Cancel
                </button>
              </div>
            </div>

            <div>
              <span class="block text-sm font-medium text-gray-500 mb-1">Expected close date</span>

              <!-- Mod display: data + buton edit -->
              <div v-if="!editExpectedCloseDate" class="flex items-center gap-2 group">
                <span class="text-sm font-medium text-gray-900">
                  {{ formatDate(lead.expected_close_date) || '—' }}
                </span>
                <button
                  @click="toggleEditExpectedCloseDate"
                  class="p-1 rounded text-gray-400 hover:text-blue-600 hover:bg-blue-50 transition opacity-0 group-hover:opacity-100"
                  title="Edit date"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" class="w-4 h-4">
                    <path
                      fill="currentColor"
                      d="M1 4c0-1.1.9-2 2-2h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V4zm2 2v12h14V6H3zm2-6h2v2H5V0zm8 0h2v2h-2V0zM5 9h2v2H5V9zm0 4h2v2H5v-2zm4-4h2v2H9V9zm0 4h2v2H9v-2zm4-4h2v2h-2V9zm0 4h2v2h-2v-2z"
                    />
                  </svg>
                </button>
              </div>

              <!-- Mod edit: input + cancel -->
              <div v-else class="flex items-center gap-2">
                <input
                  type="date"
                  v-model="expected_close_date"
                  @change="updateExpectedCloseDate"
                  class="text-sm px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent cursor-pointer"
                />
                <button
                  @click="toggleEditExpectedCloseDate"
                  class="text-xs text-gray-500 hover:text-gray-700"
                >
                  Cancel
                </button>
              </div>
            </div>

            <template v-if="lead.status === 'lost'">
              <div>
                <span class="block text-sm font-medium text-gray-500 mb-1">Lost reason</span>
                <span class="block text-base font-semibold text-gray-900">
                  {{ lead.lost_reason?.name ?? 'N/A' }}
                </span>
              </div>

              <div>
                <span class="block text-sm font-medium text-gray-500 mb-1"
                  >Lost reason details</span
                >
                <span class="block text-base font-semibold text-gray-900">
                  {{ lead.lost_reason_details || 'N/A' }}
                </span>
              </div>

              <div>
                <span class="block text-sm font-medium text-gray-500 mb-1">Lost at</span>
                <span class="block text-base font-semibold text-gray-900">
                  {{ formatDate(lead.lost_at) ?? 'N/A' }}
                </span>
              </div>
            </template>

            <div v-if="lead.address" class="sm:col-span-2 lg:col-span-3">
              <span class="block text-sm font-medium text-gray-500 mb-1">Address</span>
              <span class="block text-base font-semibold text-gray-900">
                {{ lead.address.country }}, {{ lead.address.county }}, {{ lead.address.city }},
                {{ lead.address.street }} {{ lead.address.street_number }}, building:
                {{ lead.address.building }}, floor: {{ lead.address.floor }}, apt.
                {{ lead.address.apartment_number }}
              </span>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8 pt-6 border-t border-gray-100">
          <div>
            <span class="block text-xs font-medium text-gray-400 mb-1">Created at</span>
            <span class="block text-sm text-gray-600">{{ formatDate(lead.created_at) }}</span>
          </div>
          <div>
            <span class="block text-xs font-medium text-gray-400 mb-1">Last modified</span>
            <span class="block text-sm text-gray-600">{{ formatDate(lead.modified_at) }}</span>
          </div>
          <div>
            <span class="flex text-xs font-medium text-gray-400 mb-1">Days since created</span>
            <span class="flex text-sm text-gray-600">{{
              calculateDaysFromToday(lead.created_at) + ' days'
            }}</span>
          </div>
          <div>
            <span class="flex text-xs font-medium text-gray-400 mb-1">Days from last update</span>
            <span class="flex text-sm text-gray-600">{{
              calculateDaysFromToday(lead.modified_at) + ' days'
            }}</span>
          </div>
        </div>
      </div>

      <!-- Lead Task -->
      <div class="bg-white border border-gray-200 shadow-md rounded-2xl p-6 md:p-8 w-1/3">
        <div
          class="flex items-center justify-between text-gray-800 mb-6 border-b border-gray-100 pb-4"
        >
          <h1 class="text-xl font-bold">Tasks</h1>
          <button class="font-bold text-lg" @click="toggleaddTaskModal">
            <img
              src="/icons/add-square-svgrepo-com.svg"
              alt="addTask"
              class="w-6 h-6 rounded-lg hover:w-5 hover:h-5"
            />
          </button>
        </div>

        <div v-if="taskStore.leadTasks.length > 0" class="max-h-[350px] overflow-y-auto space-y-2">
          <div v-for="task in taskStore.leadTasks" :key="task.title">
            <div class="bg-white border border-gray-200 shadow-md rounded-2xl p-6">
              <h1 class="bg-blue-950 text-white font-bold rounded-lg p-1">{{ task.title }}</h1>
              <p class="p-2">{{ task.description }}</p>
              <div class="flex justify-end items-center gap-1">
                <!-- Show more -->
                <button
                  @click="toggleLeadDetail(task)"
                  class="group hover:cursor-pointer w-8 h-8 flex items-center justify-center"
                >
                  <img
                    src="/icons/show-more-horizontal-svgrepo-com.svg"
                    alt="showMore"
                    class="w-5 h-5 transition-all group-hover:brightness-0 group-hover:[filter:invert(27%)sepia(100%)saturate(500%)hue-rotate(190deg)]"
                  />
                </button>

                <!-- Play -->
                <button
                  v-if="task.status === 'open'"
                  @click="startTask(task.id)"
                  class="group cursor-pointer w-8 h-8 flex items-center justify-center"
                  :style="task.status === 'inprogress' ? 'cursor: not-allowed' : ''"
                >
                  <img
                    src="/icons/play-svgrepo-com.svg"
                    class="w-4 h-4 transition-all group-hover:brightness-0 group-hover:[filter:invert(50%)sepia(100%)saturate(400%)hue-rotate(90deg)]"
                    alt="start"
                  />
                </button>

                <!-- Check -->
                <button
                  v-if="task.status !== 'closed'"
                  @click="taskDone(task.id)"
                  class="group hover:cursor-pointer w-8 h-8 flex items-center justify-center"
                >
                  <img
                    src="/icons/check-read-svgrepo-com.svg"
                    alt="checked"
                    class="w-5 h-5 transition-all group-hover:brightness-0 group-hover:[filter:invert(50%)sepia(100%)saturate(400%)hue-rotate(90deg)]"
                  />
                </button>

                <button
                  @click="handleDeleteTask(task.id)"
                  class="group hover:cursor-pointer w-8 h-8 flex items-center justify-center"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4 text-gray-500 transition-colors group-hover:text-red-500"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                    />
                  </svg>
                </button>
              </div>
              <div v-if="activeTask === task.id">
                <p class="pl-2">Status: {{ task.status }}</p>
                <p class="pl-2">Due date: {{ formatDate(task.due_date) }}</p>
                <p class="pl-2">Days left: {{ daysLeft(task.due_date) }}</p>
                <p class="pl-2">
                  <span class="font-bold">Member:</span> {{ task.assigned_to.last_name }}
                  {{ task.assigned_to.first_name }}
                </p>
              </div>
            </div>
          </div>
          <div>
            <h1
              class="mt-2 align-lg-end justify-end text-medium font-bold text-gray-800 mb-6 border-b border-gray-100 pb-4text-xl pb-4"
            >
              Summary
            </h1>
          </div>
        </div>
        <div v-else>
          <p
            class="flex align-center justify-center font-semibold bg-blue-900 text-white rounded-lg p-1"
          >
            No tasks for this lead!
          </p>
        </div>
      </div>
    </div>

    <DefaultModal :modalActive="addTaskModal" @close-modal="toggleaddTaskModal">
      <div class="mt-10 bg-white shadow-md rounded-xl border border-gray-200 overflow-hidden">
        <form @submit.prevent="">
          <div class="px-6 py-4 border-b border-gray-200">
            <h1 class="text-xl font-bold mb-2">Add task</h1>

            <label class="block text-medium font-semibold mb-1">Title</label>
            <input
              type="text"
              class="rounded-lg border-gray-200 w-full"
              placeholder="Task title..."
              v-model="taskTitle"
            />
            <label class="block text-medium font-semibold mb-1">Description</label>
            <textarea
              class="rounded-lg border-gray-200 w-full"
              v-model="taskDescription"
              placeholder="Description..."
            ></textarea>
            <label class="block text-medium font-semibold mb-1">Due date:</label>
            <input
              type="datetime-local"
              class="rounded-lg border-gray-200 w-full"
              v-model="taskDueDate"
            />
            <label class="block text-medium font-semibold mb-1">Assigned to:</label>
            <select
              id="countries"
              class="block w-2/3 px-3 py-2.5 bg-transparent border-l-gray-50 border-r-gray-50 border-t-gray-50 text-heading text-sm rounded-base focus:ring-brand focus:border-brand shadow-xs placeholder:text-body"
              v-model="taskAssignedTo"
              required
            >
              <option selected>Choose member</option>
              <option v-for="member in teamStore.team.members" :key="member.id" :value="member.id">
                {{ member.first_name }} {{ member.last_name }}
              </option>
            </select>
            <button class="bg-blue-900 p-2 rounded-lg text-white mt-2 w-full" @click="addTask">
              Add task
            </button>
          </div>
        </form>
      </div>
    </DefaultModal>

    <div class="mt-10 bg-white shadow-md rounded-xl border border-gray-200 overflow-hidden">
      <div class="bg-gray-50 px-6 py-4 border-b border-gray-200">
        <div class="flex items-center">
          <h3 class="text-lg font-bold text-gray-800">Products</h3>
          <button
            @click="showAddProducts"
            type="button"
            class="ml-3 font-bold text-2xl cursor-pointer leading-none"
          >
            +
          </button>
        </div>
      </div>
      <div class="bg-gray-50 px-6 py-4 border-b border-gray-200 flex items-center justify-between">
        <ProductsLead></ProductsLead>
      </div>
    </div>
    <DefaultModal :modalActive="showAddProductModal" @close-modal="showAddProducts">
       <AssignProductComponent></AssignProductComponent>
    </DefaultModal>

    <div class="mt-10 bg-white shadow-md rounded-xl border border-gray-200 overflow-hidden">
      <div class="bg-gray-50 px-6 py-4 border-b border-gray-200">
        <h3 class="text-lg font-bold text-gray-800">Activities and notes</h3>
      </div>

      <div>
        <div
          class="bg-gray-50 px-6 py-4 border-b border-gray-200 flex items-center justify-between"
        >
          <h3 class="text-lg font-bold text-gray-800">Progress</h3>
          <button
            @click="toggleProgress"
            class="font-bold text-2xl hover:bg-white hover:cursor-pointer"
          >
            <img
              v-if="showProgress"
              src="/icons/minus.png"
              alt="-"
              class="w-3 h-3 hover:bg-white"
            />
            <img v-if="!showProgress" src="/icons/down-arrow.png" alt="show less" class="w-3 h-3" />
          </button>
        </div>
        <div
          v-if="showProgress"
          class="bg-white px-6 py-4 border-b border-gray-200 flex item item-center justify-between"
        >
          <div class="border border-gray-200 rounded-lg p-2 flex items-center justify-center gap-2">
            <h4 class="inline-block text-gray-800 font-semibold">Status pipeline</h4>
            <span class="text-gray-200 text-3xl">|</span>
            <p
              :class="progressStatus(lead.status, 'new')"
              class="bg-blue-50 text-blue-700 border rounded border-blue-200 text-center px-3 py-1"
            >
              New
            </p>
            <p
              :class="progressStatus(lead.status, 'contacted')"
              class="bg-orange-50 text-orange-700 border rounded border-orange-200 text-center px-3 py-1"
            >
              Contacted
            </p>
            <p
              :class="progressStatus(lead.status, 'inprogress')"
              class="bg-yellow-50 text-yellow-700 border rounded border-yellow-200 text-center px-3 py-1"
            >
              In progress
            </p>
            <p
              :class="progressStatus(lead.status, 'won')"
              class="bg-green-50 text-green-700 border rounded border-green-200 text-center px-3 py-1"
            >
              Won
            </p>
            <p
              :class="progressStatus(lead.status, 'lost')"
              class="bg-red-50 text-red-700 border rounded border-red-200 text-center px-3 py-1"
            >
              Lost
            </p>
          </div>
        </div>
      </div>
      <div class="p-6">
        <h3>Notes</h3>
        <form
          @submit.prevent="submitQuickNote"
          class="mb-10 bg-gray-800 p-4 rounded-lg border border-blue-100"
        >
          <div class="grid grid-cols-1 gap-4">
            <div>
              <label class="block text-xs font-semibold text-white uppercase mb-1"
                >Note title (Optional)</label
              >
              <input
                v-model="noteName"
                type="text"
                placeholder="Ex: Customer call, Office visit..."
                class="w-full p-2 text-sm border border-blue-200 rounded focus:ring-2 focus:ring-blue-400 outline-none"
              />
            </div>

            <div>
              <label class="block text-xs font-semibold text-white uppercase mb-1"
                >Detailed Description</label
              >
              <textarea
                v-model="noteBody"
                rows="3"
                placeholder="What have you discussed so far?"
                class="w-full p-3 text-sm border border-blue-200 rounded focus:ring-2 focus:ring-blue-400 outline-none"
                required
              ></textarea>
            </div>

            <div class="flex justify-end">
              <button
                type="submit"
                :disabled="isSubmitting || !noteBody.trim()"
                class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded font-medium text-sm transition-all disabled:opacity-50"
              >
                {{ isSubmitting ? 'Saving...' : 'Save note' }}
              </button>
            </div>
          </div>
        </form>

        <div v-if="leadStore.leadNotes && leadStore.leadNotes.length > 0" class="space-y-6">
          <div v-for="note in leadStore.leadNotes" :key="note.id" class="flex gap-4 group">
            <div class="flex flex-col items-center">
              <div
                class="w-3 h-3 bg-blue-500 rounded-full mt-1.5 shadow-[0_0_0_4px_rgba(59,130,246,0.1)]"
              ></div>
              <div class="w-0.5 h-full bg-gray-100"></div>
            </div>

            <div class="flex-1 pb-6">
              <div class="flex justify-between items-start">
                <div>
                  <h4 class="text-sm font-bold text-gray-900">{{ note.name }}</h4>
                  <p class="text-xs text-gray-500 mb-2">
                    Added by
                    <span class="font-semibold text-gray-700">{{
                      note.created_by_name || 'Sistem'
                    }}</span>
                    pe
                    {{ new Date(note.created_at).toLocaleString('ro-RO') }}
                  </p>
                </div>

                <button
                  @click="leadStore.deleteLeadNote(note.id, route.params.id)"
                  class="text-gray-300 hover:text-red-500 transition-colors opacity-0 group-hover:opacity-100 p-1"
                  title="Delete note"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                    />
                  </svg>
                </button>
              </div>
              <div class="bg-gray-50 p-4 rounded-xl border border-gray-100 shadow-sm mt-1">
                <p class="text-sm text-gray-700 whitespace-pre-line leading-relaxed">
                  {{ note.body }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <div v-else class="text-center py-12">
          <div
            class="inline-flex items-center justify-center w-12 h-12 rounded-full bg-gray-50 mb-3"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6 text-gray-300"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
              />
            </svg>
          </div>
          <p class="text-gray-400 text-sm">There is no activity recorded yet.</p>
        </div>
      </div>
    </div>
  </div>

  <div v-else class="flex items-center justify-center">
    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
  </div>

  <DefaultModal :modalActive="modalActive" @close-modal="toggleModal">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800 border-b pb-2">Send Mail</h2>

    <form @submit.prevent="sendMail" class="space-y-6">
      <div class="flex flex-col gap-1">
        <label for="to" class="text-sm font-medium text-gray-500 uppercase tracking-wider"
          >To:</label
        >
        <input
          type="email"
          id="to"
          v-model="emailForm.to"
          placeholder="recipient@example.com"
          class="w-full border-0 border-b-2 border-gray-200 bg-transparent py-2 px-0 focus:ring-0 focus:border-blue-600 transition-colors outline-none text-gray-700"
          required
        />
      </div>

      <div class="flex flex-col gap-1">
        <label for="subject" class="text-sm font-medium text-gray-500 uppercase tracking-wider"
          >Subject:</label
        >
        <input
          type="text"
          id="subject"
          v-model="emailForm.subject"
          placeholder="Enter subject"
          class="w-full border-0 border-b-2 border-gray-200 bg-transparent py-2 px-0 focus:ring-0 focus:border-blue-600 transition-colors outline-none text-gray-700"
          required
        />
      </div>

      <div class="flex flex-col gap-1">
        <label for="message" class="text-sm font-medium text-gray-500 uppercase tracking-wider"
          >Message:</label
        >
        <textarea
          id="message"
          v-model="emailForm.message"
          rows="3"
          placeholder="Write your message here..."
          class="w-full border-0 border-b-2 border-gray-200 bg-transparent py-2 px-0 focus:ring-0 focus:border-blue-600 transition-colors outline-none text-gray-700 resize-none"
          required
        ></textarea>
      </div>

      <div class="flex flex-col gap-2">
        <label class="text-sm font-medium text-gray-500 uppercase tracking-wider"
          >Attachments:</label
        >
        <div class="relative flex items-center">
          <input
            type="file"
            id="file"
            multiple
            @change="onFileChange"
            class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 transition-all cursor-pointer"
          />
        </div>
      </div>

      <div class="pt-4 flex justify-end">
        <button
          type="submit"
          :disabled="isLoading"
          class="bg-blue-950 text-white px-6 py-2 rounded-lg flex items-center gap-2 transition-all hover:bg-blue-900 disabled:opacity-50 disabled:cursor-not-allowed shadow-md"
        >
          <svg
            v-if="isLoading"
            class="animate-spin h-5 w-5 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              class="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
            ></circle>
            <path
              class="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>

          <span>{{ isLoading ? 'Sending...' : 'Send' }}</span>
        </button>
      </div>

      <div class="mt-4">
        <p
          v-if="error"
          class="text-red-500 text-sm text-right bg-red-50 p-2 rounded border border-red-100 italic"
        >
          {{ error }}
        </p>
        <p
          v-if="isSucces"
          class="text-green-600 text-sm font-bold text-right flex items-center justify-end gap-1"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="size-4"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 6 6 9-13.5" />
          </svg>
          Email sent successfully!
        </p>
      </div>
    </form>
    <InboxEmail :lead-id="route.params.id" class="mt-8 border-t pt-6"></InboxEmail>
  </DefaultModal>
</template>

<script setup>
import { useLeadStore } from '@/stores/leadStore.js'
import { useRoute, useRouter } from 'vue-router'
import { computed, onMounted, ref, watch } from 'vue'
import formatDate from '/services/formatDate.js'
import DefaultModal from '@/components/Modals/DefaultModal.vue'
import { useEmailStore } from '@/utils/emailStore.js'
import { storeToRefs } from 'pinia'
import InboxEmail from '@/components/Email/InboxEmail.vue'
import calculateDaysFromToday from '../../../services/calculateDaysFromToday.js'
import { useTaskStore } from '@/stores/taskStore.js'
import { useToast } from 'vue-toast-notification'
import { useTeamStore } from '@/stores/teamStore.js'
import ProductsLead from '@/components/ProductsComponents/ProductsLead.vue'
import AssignProductComponent from '@/components/ProductsComponents/AssignProductComponent.vue'

const leadStore = useLeadStore()
const taskStore = useTaskStore()

const route = useRoute()
const router = useRouter()
const lead = computed(() => leadStore.lead)
const checklist_data = computed(() => leadStore.lead.checklist)
const noteName = ref('')
const noteBody = ref('')
const isSubmitting = ref(false)
const showChecklist = ref(false)
const teamStore = useTeamStore()
const toggleCheklist = () => {
  showChecklist.value = !showChecklist.value
}

const leadCannotBeModifiedError = new Error(
  'This lead cannot be modified! The status is an end status : [WON / LOST].',
)

const showProgress = ref(true)
const toggleProgress = () => {
  showProgress.value = !showProgress.value
}

const showMoreDetails = ref(false)
const toggleMoreDetails = () => {
  showMoreDetails.value = !showMoreDetails.value
}

const emailStore = useEmailStore()
const { isLoading, error, isSucces } = storeToRefs(emailStore)

const modalActive = ref(false)
const toggleModal = () => {
  modalActive.value = !modalActive.value
}

const submitQuickNote = async () => {
  if (!noteBody.value.trim() && !noteName.value.trim()) return
  isSubmitting.value = true

  const formData = {
    lead_id: route.params.id,
    name: noteName.value.trim()
      ? `${noteName.value} - ${new Date().toLocaleDateString('ro-RO')}`
      : `Notă - ${new Date().toLocaleDateString('ro-RO')}`,
    body: noteBody.value,
  }

  try {
    await leadStore.postLeadNote(formData)
    noteBody.value = ''
    noteName.value = ''
  } catch (err) {
    console.error('Erroar while sending the note!', err)
  } finally {
    isSubmitting.value = false
  }
}

const contactMethods = [
  { value: 'Phone', label: 'Phone' },
  { value: 'Email', label: 'Email' },
]

const getStatusColor = (status) => {
  const colors = {
    new: 'bg-blue-50 text-blue-700 border-blue-200',
    contacted: 'bg-orange-50 text-orange-700 border-orange-200',
    inprogress: 'bg-yellow-50 text-yellow-700 border-yellow-200',
    lost: 'bg-red-50 text-red-700 border-red-200',
    won: 'bg-green-50 text-green-700 border-green-200',
  }
  return colors[status] || 'bg-gray-50 text-gray-700 border-gray-200'
}

const progressStatus = (status, currentElement) => {
  const statusList = ['new', 'contacted', 'inprogress', 'lost', 'won']
  let progressColor = {}
  if (!statusList.includes(status)) {
    progressColor = 'bg-gray-700 text-white font-bold'
  }

  if (currentElement === status && status === 'new') {
    progressColor = 'bg-blue-700 text-white font-bold rounded p-1'
  } else if (currentElement === status && status === 'contacted') {
    progressColor = 'bg-orange-700 text-white font-bold rounded p-1'
  } else if (currentElement === status && status === 'inprogress') {
    progressColor = 'bg-yellow-700 text-white font-bold rounded p-1'
  } else if (currentElement === status && status === 'lost') {
    progressColor = 'bg-red-700 text-white font-bold rounded p-1'
  } else if (currentElement === status && status === 'won') {
    progressColor = 'bg-green-700 text-white font-bold rounded p-1'
  }

  return progressColor
}

const submitChecklist = async () => {
  try {
    console.log(leadStore.lead.checklist)
    await leadStore.editLead(route.params.id, {
      checklist: checklist_data.value,
    })
  } catch (err) {
    console.error('Cannot save the checklist', err)
  }
}

onMounted(async () => {
  const id = route.params.id
  await leadStore.getLead(id)
  await leadStore.getLeadNotes(id)
  await taskStore.getLeadTask(id)
  await teamStore.fetchTeam()
  console.log(leadStore.lead)

  if (lead.value && lead.value.email) {
    emailForm.value.to = lead.value.email
  }
})

const handleDelete = async () => {
  if (confirm('Are you sure that you want to delete the lead? ')) {
    try {
      await leadStore.deleteLead(route.params.id)
      leadStore.showMessage('Lead sters cu succes!')
      router.push('/dashboard/leads')
    } catch (err) {
      alert('Cannot delete the lead')
      console.log(err)
    }
  }
}

const handleConvert = async () => {
  if (confirm('Are you sure you want to convert the lead?')) {
    await leadStore.convertToClient(route.params.id)
    await router.push({ name: 'Clients' })
  }
}

watch(
  lead,
  (newVal) => {
    if (newVal && newVal.company) {
      document.title = `Details: ${newVal.company} | Lead Details`
    }
  },
  { immediate: true },
)

// Sending email

const emailForm = ref({
  to: '',
  subject: '',
  message: '',
  files: null,
  lead: route.params.id,
})

const onFileChange = (e) => {
  emailForm.value.files = e.target.files
}

const sendMail = async () => {
  const ok = await emailStore.sendAndSaveMail(emailForm.value)

  if (ok) {
    emailForm.value = { to: '', subject: '', message: '', files: null, lead: route.params.id }
  }
}

// Tasks

const addTaskModal = ref(false)
const activeTask = ref(null)

const toggleLeadDetail = (task) => {
  activeTask.value = activeTask.value === task ? null : task.id
}

const toggleaddTaskModal = () => {
  addTaskModal.value = !addTaskModal.value
}

const daysLeft = (date) => {
  const due_date = new Date(date)
  const today = Date.now()
  const days = (due_date - today) / (1000 * 60 * 60 * 24)
  return Math.ceil(days) // rounds
}

const toast = useToast()

const handleDeleteTask = async (taskID) => {
  const ok = confirm('Are you sure that you want to delete the task? ')
  if (ok) {
    await taskStore.deleteTask(taskID)
    toast.success('Task deleted successfully!')
  }
}

const startTask = async (taskId) => {
  const newStatus = {
    status: 'inprogress',
  }

  const success = await taskStore.changeStatus(taskId, newStatus)
  if (success) {
    toast.success(`Task started successfully!`)
  } else {
    toast.error('Error while starting the task, please try again.')
  }
}

const taskDone = async (taskId) => {
  const newStatus = {
    status: 'closed',
  }
  const success = await taskStore.finishTask(taskId, newStatus)
  if (success) {
    toast.success('Task finished successfully!')
  } else {
    toast.error('Error while finishing the task, please try again.')
  }
}

const taskTitle = ref('')
const taskDescription = ref('')
const taskDueDate = ref('')
const taskAssignedTo = ref('')

const addTask = async () => {
  const formData = {
    title: taskTitle.value,
    description: taskDescription.value,
    due_date: taskDueDate.value,
    lead_id: route.params.id,
    assigned_to: taskAssignedTo.value,
  }

  try {
    if (leadStore.lead.status === 'won' || leadStore.lead.status === 'lost') {
      throw leadCannotBeModifiedError
    }
    const success = await taskStore.createTask(formData)
    if (success) {
      toast.success('Task created succesfully!')
    }
  } catch (err) {
    console.error(err.message)
    toast.error('Error while creating the task! Please try again..')
  } finally {
    toggleaddTaskModal()
  }
}

const next_follow_up_date = ref('')
const updateFollowUpDate = async () => {
  const follow_up_date = {
    next_follow_up_date: next_follow_up_date.value,
  }
  try {
    if (leadStore.lead.status === 'won' || leadStore.lead.status === 'lost') {
      throw leadCannotBeModifiedError
    }
    await leadStore.editLead(route.params.id, follow_up_date)
    toast.success('Follow up date updated successfully!')
  } catch (err) {
    console.error(err)
    toast.error('Error while updating next follow up date!')
  }
}

const editFollowUpDate = ref(false)
const toggleEditFollowUpDate = () => {
  editFollowUpDate.value = !editFollowUpDate.value
}

const editExpectedCloseDate = ref(false)
const toggleEditExpectedCloseDate = () => {
  editExpectedCloseDate.value = !editExpectedCloseDate.value
}

const expected_close_date = ref('')
const updateExpectedCloseDate = async () => {
  try {
    if (leadStore.lead.status === 'won' || leadStore.lead.status === 'lost') {
      throw leadCannotBeModifiedError
    }

    const expectedCloseDate = {
      expected_close_date: expected_close_date.value,
    }

    await leadStore.editLead(route.params.id, expectedCloseDate)
    toast.success('Expected close date updated successfully!')
  } catch (err) {
    toast.error(err.message)
    console.error(err)
  }
}

// Show all prducts
const showAddProductModal = ref(false)

const showAddProducts = () => {
  showAddProductModal.value = !showAddProductModal.value
}
</script>
