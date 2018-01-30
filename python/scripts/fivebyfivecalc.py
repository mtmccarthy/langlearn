import datetime, sys

firstADay = datetime.date(year=2018, month=1, day=10)
extraRestDays = 0
firstBDay = datetime.date(year=2018,month=1, day=8)
workoutBTemplate = (155, 90, 175)
workoutATemplate = (160, 115, 120)

def main():
  year = int(sys.argv[1])
  month = int(sys.argv[2])
  day = int(sys.argv[3])
  compareDate = datetime.date(year=year,month=month,day=day)
  deltaA = compareDate - firstADay
  deltaB = compareDate - firstBDay
  daysBetweenA = deltaA.days - extraRestDays
  daysBetweenB = deltaB.days - extraRestDays

  if(daysBetweenA % 4 == 0):
    totalWorkouts = daysBetweenA / 2;
    aWorkouts = daysBetweenA / 4;
    squat = workoutBTemplate[0] + 5*totalWorkouts  
    print("Squat: ", squat)
    ohp = workoutBTemplate[1] + 5*aWorkouts
    print("OHP: ", ohp)
    deadlift = workoutBTemplate[2] + 10*aWorkouts
    print("Deadlift: ", deadlift)
  elif(daysBetweenB % 4 == 0):
    workouts = daysBetweenA / 2; 
    bWorkouts = daysBetweenB / 4;
    squat = workoutBTemplate[0] + 5*workouts  
    print("Squat: ", squat)
    bench = workoutATemplate[1] + 5*bWorkouts
    print("Benchpress: ", bench)
    row = workoutATemplate[2] + 5*bWorkouts
    print("BarbellRow: ", row)
  else:
    print("Not a workout day")

if __name__ == "__main__":
  main()


