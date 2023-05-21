console.log("hello word")

const form2=document.getElementById("formEnviar");

console.log(form2)

form2.addEventListener('submit',(ev)=>{
    console.log("evento",ev);
    ev.preventDefault()
    const formData=form2.querySelector('input[name="email"]')
    const formdata2=new FormData(form2)
    console.log(formdata2.get("email"))
    console.log(formData)
})