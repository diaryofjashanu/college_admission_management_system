const form = document.querySelector("form");
fileInput = form.querySelector(".file-input");
progressArea = document.querySelector(".progress-area");
uploadedArea = document.querySelector(".uploaded-area");

form.addEventListener("click",()=>{
    fileInput.click();
});

fileInput.onchnage = e =>{
    let file = target.files[0];
    if(file){
        let fileName = file.name;
        uploadfile(filename)
    }
}





















