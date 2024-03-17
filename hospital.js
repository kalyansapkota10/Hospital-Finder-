
function hospital_list(){
    // Fetch hospital data from the API
    fetch('https://7c19-2400-1a00-b080-9bb8-669e-f7c9-8451-7593.ngrok-free.app/specialty/9/Hospital_Json_Response')
       .then(response => response.json())
       .then(data => displayHospitals(data))
       .catch(error => console.error('Error fetching hospital data:', error));
 }
 
 function displayHospitals(hospitals) {
    const hospitalListElement = document.getElementById('hospitalList');
 
    hospitals.forEach(hospital => {
       const hospitalDiv = document.createElement('div');
       hospitalDiv.innerHTML = `<h2>${hospital.name}</h`;
       hospitalListElement.appendChild(hospitalDiv);
    });
 }

 hospital_list()
 