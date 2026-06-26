
function inactiveStatusCount(entities){
  let inactiveEntity = 0
  for (let entity of entities){
    if(entity.status == 'inactive'){
      inactiveEntity++
    }
  }
  console.log(inactiveEntity)
  return inactiveEntity
}

export default inactiveStatusCount
