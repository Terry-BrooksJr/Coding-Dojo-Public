const calendarEl = document.querySelector('.calendar');
const daySelectEl = document.querySelector('#firstdayoftheweek');
const yearSelectEl = document.querySelector('#year');
const yearTitleEl = document.querySelector('#yeartitle');
const monthOptions = [
  {color: "#007cbc", icon: "2744"},
  {color: "#0099d2", icon: "2665"},
  {color: "#009d50", icon: "1f337"},
  {color: "#74ad38", icon: "1f95a"},
  {color: "#8ea01c", icon: "273f"},
  {color: "#eca90f", icon: "e0ec"},
  {color: "#e8860e", icon: "1f9f3"},
  {color: "#ed3408", icon: "1f334"},
  {color: "#e22b4f", icon: "1f34e"},
  {color: "#b3347c", icon: "f707"},
  {color: "#6f3e97", icon: "1f341"},
  {color: "#433d97", icon: "1f384"}, 
]


const dateNow = new Date();
let year = dateNow.getFullYear()
const today = new Date(dateNow.getFullYear(), dateNow.getMonth(), dateNow.getDate());
let firstDayOfTheWeek;

(async()=>{  
  if(localStorage.getItem('firstDayOfTheWeek')){
    firstDayOfTheWeek = Number(localStorage.getItem('firstDayOfTheWeek'))
  } else {
    try{
      // coutryCode by IP
      const result_ip = await fetch('http://ip-api.com/json?fields=countryCode');
      const {countryCode} = await result_ip.json();
      // first day per country ref https://github.com/unicode-cldr/cldr-core/blob/master/supplemental/weekData.json#L61
      const result_week = await fetch('https://raw.githubusercontent.com/unicode-cldr/cldr-core/master/supplemental/weekData.json');
      const data_week = await result_week.json();
      const firstDayCode = data_week.supplemental.weekData.firstDay[countryCode];
      firstDayOfTheWeek = ['sun','mon','thu','wed','thu','fri','sat'].indexOf(firstDayCode) || 1;
    } catch (error) {
      console.log(error)
      firstDayOfTheWeek = 1;
    }
  }
  initYearSelect();
  initFistDayOfTheWeekSelect()
  initCalendar();
})()

function initYearSelect(){
  yearSelectEl.value = year;
  yearTitleEl.textContent = year
}
function initCalendar(){
  calendarEl.innerHTML = '';
  //create calendar
  for(let monthIndex = 0; monthIndex < 12; monthIndex++){
    
    const firstDay = new Date(year, monthIndex, 1);
    const lastDay = new Date(year, monthIndex+1, 0);
    const strMonthNumber = String(monthIndex+1).padStart(2,'0');
    const strMonthName = firstDay.toLocaleString('default', { month: 'long' });

    //monthEl
    const monthEl = el('div','month');
    monthEl.style.setProperty(`--monthColor`, monthOptions[monthIndex].color)
    monthEl.style.setProperty(`--monthIcon`, `'\\${monthOptions[monthIndex].icon}'`)
    calendarEl.append(monthEl);

    //titleEl
    const titleEl = el('div', 'title');
    titleEl.textContent = strMonthName;
    
    //daysEl
    const dayNames = getDaysInLocalString('short', firstDayOfTheWeek);
    const daysEl = el('div', 'days');
    dayNames.forEach(day => {
      const dayEl = el('div', 'day');
      dayEl.textContent = day;
      daysEl.append(dayEl);
    })

    //datesEl
    const datesEl = el('div', 'dates');
    for(let dateIndex = 0; dateIndex < lastDay.getDate(); dateIndex++){
      
      const date = new Date(year, monthIndex, dateIndex +1);
      const dateEl = el('div', 'date');
      //determin first date day
      if(dateIndex == 0) dateEl.style.setProperty('--dayColumn', (date.getDay() - firstDayOfTheWeek + 7) % 7 + 1)
      //check today
      if(date.toLocaleString()==today.toLocaleString()) dateEl.classList.add('today')
      
      dateEl.textContent = date.getDate();
      datesEl.append(dateEl);
    }
    monthEl.append(titleEl, daysEl,datesEl)
  }
}

function el(tag, className = false){
  const el = document.createElement(tag);
  if(className) el.className = className;
  return el;
}

function getDaysInLocalString(length='long', initialFirstDay = 1){
  const date = new Date(year, 0, 1);
  const dayNames = Array.from(Array(7),(_,i)=>{
    return new Date(year, 0, date.getDate() - date.getDay() + 7 + i + initialFirstDay).toLocaleString('default', {weekday: length});
  })
  return dayNames
}

function initFistDayOfTheWeekSelect(){
  //first day of the week options
  const dayOptions = getDaysInLocalString('long', 1);
  dayOptions.forEach((day,index)=>{
    if([0,5,6].includes(index)){
      const optionEl = el('option');
      optionEl.value = (index + 1)%7;
      if(optionEl.value == firstDayOfTheWeek) optionEl.selected = true
      optionEl.textContent = day;
      daySelectEl.append(optionEl)
    }
  })
  daySelectEl.addEventListener('change', ()=>{
    if(Number(daySelectEl.value) === firstDayOfTheWeek) return; //return if nothing changed
    firstDayOfTheWeek = Number(daySelectEl.value);
    localStorage.setItem('firstDayOfTheWeek', daySelectEl.value);
    initCalendar();
  })
}


function setYear(increment=false){
  let value = 0;
  if(increment) value = year += increment
  else value = Number(yearSelectEl.value)

  if(value >= 1900 && value <= 2100) {
    year = value;
    yearSelectEl.value = value;
    yearTitleEl.textContent = value;
    initCalendar();
  }
}