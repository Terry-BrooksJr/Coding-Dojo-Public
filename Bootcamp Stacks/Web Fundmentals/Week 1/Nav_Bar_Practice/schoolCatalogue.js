class School {
  constructor(name, level, numberOfStudents) {
    this._name = name;
    this._level = level;
    this._numberOfStudents = numberOfStudents;
  }
  get name() {
    return this._name
  }
  get level() {
    return this._level
  }
  get numberOfStudents() {
    return this._numberOfStudents
  }
  set numberOfStudents(newNumberOfStudents) {
    if (newNumberOfStudents.isNaN()) {
      console.log('Invalid input: numberOfStudents must be set to a Number.')
    } else {
      this._numberOfStudents = newNumberOfStudents;
  }
}
  get quickFacts() {
    console.log(`${this._name} educates ${this._numberOfStudents} students at the ${this._level} school level.`)
  }
  static pickSubstituteTeacher(substituteTeachers) {
    const randInt = Math.floor(Math.random() * substituteTeachers.length);
    return substituteTeachers[randInt]

  }
}
class PrimarySchool extends School{
  constructor(name, numberOfStudents, pickupPolicy){
    super(name, 'primary', numberOfStudents);
    this._pickupPolicy = pickupPolicy;
    }
    get pickupPolicy(){
      return this._pickupPolicy
  }
}
class HighSchool extends School{
  constructor(name, numberOfStudents, sportsTeam){
    super(name, 'high', numberOfStudents);
    this._sportsTeam = sportsTeam;
    }
    get sportsTeam(){
      return this.sportsTeam
  }
}
class MiddleSchool extends School{
  constructor(name, numberOfStudents){
    super(name, 'middle', numberOfStudents);
    }
}

const lorraineHansbury = new PrimarySchool('Lorraine Hansbury',514,'Students must be picked up by a parent, guardian, or a family member over the age of 13.')
const serenaHills = new PrimarySchool('Serena Hills',632,'Student can be picked up by anyone!')
const parkerJrHigh = new MiddleSchool('Parker Junior High',880)
const hfHighSchool = new HighSchool('Homewood-Flossmoor',1300,['Baseball','Tennis','Golf','Drama'] )
