
async function analyze() {

    let fileInput = document.getElementById("resume");
    let jobdesc = document.getElementById("jobdesc").value;

    // check if resume uploaded
    if(fileInput.files.length === 0){
        alert("Please upload a resume");
        return;
    }

    let file = fileInput.files[0];

    let formData = new FormData();
    formData.append("resume", file);
    formData.append("jobdesc", jobdesc);

    try{

        let response = await fetch("http://127.0.0.1:5002/analyze",{
            method:"POST",
            body:formData
        });

        let data = await response.json();

        document.getElementById("result").innerHTML =
        "Match Score: " + data.score.toFixed(2) + "%";

    }

    catch(error){

        document.getElementById("result").innerHTML =
        "Error connecting to server";

    }
}