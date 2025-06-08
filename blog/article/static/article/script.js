window.addEventListener(
    'load',
    Main
)

function Main(){
let btn = document.querySelector('button')

btn.addEventListener(
    'click',
    ()=>{
        let adress = document.querySelector('input').value
        console.log(adress);
        // console.log(`http://127.0.0.1:8000/${adress}`);
        fetch('http://127.0.0.1:8000/' + adress).then(
            (response)=>{
                if (response.status == 200){
                    return response.text()
                }
                else{
                    console.log('Error');
                    
                }         
            }
        ).then(
            (data)=>{
                console.log(data);
                
            }
        )
    }
)
}