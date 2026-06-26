export default function calculateDaysFromToday(startDate){
  let currentDate = new Date()

  let start = new Date(startDate)

  let timeDifference = currentDate - start

  let daysDifference = Math.ceil(timeDifference / (1000 * 3600 * 24))

  return daysDifference
}
