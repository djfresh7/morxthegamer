class StopError extends Error {
  constructor(error){
    super(error)
  }
}

const classes = [
  "1. English A", "2. English B", '3. Mathematics', "4. Information Technology", "5. Industrial Techniques",
  "6. History", "7. Spanish", "8. Business Basics", "9. Geography", "10. Chemistry", "11. Religious Education", "12. Social Studies",
  "13. Biology", "14. Physics", "15. Physical Education", "16. Visual Arts", "Devotion"
]

const timeTable = {
  monday: [
    "English B",
    "Mathematics",
    "Information Technology",
    "Industrial Techniques/Visual Arts",
    "Spanish",
    "History"
  ],
  tuesday: [
    "Business Basics/Information Technology",
    "Spanish",
    "Geography",
    "Mathematics",
    "Chemistry",
    "English B"
  ],
  wednesday: [
    "English A",
    "Religious Education",
    "Social Studies",
    "Biology",
    "History",
    "Geography"
  ],
  thursday: [
    "Devotion",
    "Biology",
    "Physics",
    "Mathematics",
    "English A",
    "Business Basics/Information Technology"
  ],
  friday: [
    "Physics",
    "Religious Education",
    "Physical Education",
    "Industrial Techniques/Visual Arts",
    "Social Studies",
    "Chemistry"
  ],
}

const linksForClasses = {
  english: {
    platform: "Zoom",
    meetingLink: "https://us04web.zoom.us/j/74818486972?pwd=V0pJcUVldEFYRFNIblpxeEZNbE1hUT09",
    meetingID: 74818486972,
    meetingPassword: "iN81rC"
  },
  mathematics: {
    platform: "Zoom",
    meetingLink: "https://zoom.us/j/97988146703?pwd=bzRhR0c1UkhDdnVXc2FjTDRlTWppZz09",
    meetingID: 97988146703,
    meetingPassword: "z21qGy"
  },
  informationTech: {
    platform: "Meet",
    meetingLink: "https://meet.google.com/fgx-mwmc-dkk",
  },
  industrialTech: {
    platform: "Meet",
    meetingLink: "https://meet.google.com/lookup/bg45v4yx5f",
  },
  history: {
    platform: "Zoom",
    meetingLink: "https://us04web.zoom.us/j/5845868826?pwd=SkQ0WjZDWnhpazYyb2twTSszVjdPQT09",
    meetingID: 5845868826,
    meetingPassword: 581590
  },
  spanish: {
    platform: "Zoom",
    meetingLink: "https://zoom.us/j/98477399346?pwd=cDcweTZ6bVQyODJGc25NZ2ppZEczZz09",
    meetingID: 98477399346,
    meetingPassword: "2uA96G"
  },
  businessBasics: {
    platform: "Zoom",
    meetingLink: "https://us05web.zoom.us/j/2246790735?pwd=V3lPMDZJZmdqc2poZEJKUkVoMkgxdz09",
    meetingID: 2246790735,
    meetingPassword: "zis91T"
  },
  geography: {
    platform: "Zoom",
    meetingLink: "https://us04web.zoom.us/j/73731449787?pwd=YzEzT05YYUk5V1FvZnFzemZnanMvZz09",
    meetingID: 73731449787,
    meetingPassword: "1DMZFB"
  },
  chemistry: {
    platform: "Zoom",
    meetingLink: "https://us04web.zoom.us/j/77397831411?pwd=TGJyZGFyOWdCb3cxVi9uOFZKTVFWUT09",
    meetingID: 77397831411,
    meetingPassword: "CHEMISTRY"
  },
  religiousEducation: {
    platform: "Zoom",
    meetingLink: "https://us04web.zoom.us/j/79140628605?pwd=L3cySnZaMGdKSnVncE05ZER1cFhKdz09",
    meetingID: 79140628605,
    meetingPassword: "9Hardie"
  },
  socialStudies: {
    platform: "Meet or Zoom",
    meetingLink: "https://meet.google.com/syy-xnhb-qjw?authuser=3",
    meetingID: 5354299883,
    meetingPassword: 010675
  },
  biology: {
    platform: "Zoom",
    meetingLink: "https://us04web.zoom.us/j/71947992345?pwd=b2N1SDNydUwwaWtVZ3M3R3VmbW1sQT09",
    meetingID: 71947992345,
    meetingPassword: "RJt036"
  },
  physics: {
    platform: "Zoom",
    meetingLink: "https://us04web.zoom.us/j/74017778579?pwd=bXRYQVVhKytjSHdLT3JONHAxVVBSUT09",
    meetingID: 74017778579,
    meetingPassword: "1emQGS"
  },
  physicalEducation: {
    platform: "Zoom",
    meetingLink: "https://us04web.zoom.us/j/2623347691?pwd=U1FnMlZlZ3E1cWRnbVJyekZ5RlBNUT09",
    meetingID: 2623347691,
    meetingPassword: 656526
  },
  visualArts: {
    platform: "Zoom",
    meetingLink: "https://us04web.zoom.us/j/72413236189?pwd=UG9KcExzTmJleU1RTmJ6ODNUSzI3dz09",
    meetingID: 72413236189,
    meetingPassword: "s2x3uw"
  },
  devotion: {
    platform: "Zoom",
    meetingLink: "https://us02web.zoom.us/j/88036648547?pwd=RzdneVdxMlM5M3dsRklRWDNsVUdBZz09",
    meetingID: 88036648547,
    meetingPassword: 138910
  }
}

module.exports = { classes, linksForClasses, timeTable, StopError }