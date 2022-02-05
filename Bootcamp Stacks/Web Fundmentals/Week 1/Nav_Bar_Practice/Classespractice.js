class Media{
  constructor(title){
    this._title = title;
    this._isCheckedOut = false;
    this._ratings = [];
  }
  get title(){
    return this._title;
  }
   get isCheckedOut(){
    return this._isCheckedOut;
   }
   get ratings(){
    return this._ratings;
  }
  set isCheckedOut(value){
    this._isCheckedOut = value;
  }
  toggleCheckOutStatus(){
    this._isCheckedOut = !this.isCheckedOut;
  }
  getAverageRating(){
    let ratingsSum =
      this._ratings.reduce((accumulator, rating) => accumulator + rating);
      return ratingSum / this.ratings.length;
  }
  addRating(value){
    this._rating.push(value)
  }
  }
  class Book extends Media{
     constructor(author,title,pages){
       super(title);
  }
      get author(){
        return this._author
      }
      get pages(){
        return this._pages
      }
  }
class Movie extends Media{
    constructor(director,title,runTime){
      super(title);
    }
    get director(){
      return this._director
    }
    get runTime(){
      return this._runTime
    }
    get title(){
      return this._title
    }
}
class CD extends Media{
    constructor(singer,title,runTime){
      super(title);
    }
    get director(){
      return this._singer
    }
    get runTime(){
      return this._runTime
    }
    get title(){
      return this._title
    }
}

const historyOfEverything = new Book('Bill Bryson','A Short History of Nearly Everything',544);
historyOfEverything.toggleCheckOutStatus();
console.log(historyOfEverything.isCheckedOut())


const speed = new Movie('Jan de Bont','Speed',116)
speed.toggleCheckOutStatus();
console.log(speed.isCheckedOut())
