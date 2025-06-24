function fetch_new_posts() {
    
    dtn = new Date()
    nowDate = `${dtn.getFullYear()}-${dtn.getMonth()+1}-${dtn.getDate()}+${dtn.getHours()}:${dtn.getMinutes()}:${dtn.getSeconds()}`
    // 'last_posts/?dt=2025-06-10+21:45'

    fetch(`last_posts/?dt=${nowDate}`

    ).then((response) => {
        if (response.status == 200) {
            return response.json()
        }
    }).then((data) => {  // {'posts': [{'user': 'u1', 'text': 't1', 'title': 'smth', 'dt': 'some dt'}]}
        console.log(data)
        let h1;
        for (let p of data.posts) {
            h1 = document.createElement('h1')
            h1.style.color='green'
            h1.textContent = p.dt + ': ' + p.user + ' создал ' + p.title
            document.body.prepend(h1)
            
        }
        
    })
}

function edit_text(){
    edit_btns = document.querySelectorAll('.edit')

    edit_btns.forEach(btn => {
        btn.addEventListener(
        'click',
        ()=>{
            article = btn.closest('.div_article')
            title = article.querySelector('h1')
            text = article.querySelector('p')

            title.setAttribute('contenteditable', 'true')
            text.setAttribute('contenteditable', 'true')

            save = article.querySelector('.save')
            console.log(save);
            
            save.style.visibility = 'visible'

            articleId = article.dataset.id;

            fetch(`article/update/${articleId}/`)
            .then((response) => {
            if (response.status == 200) {
            return response.json()
            } }).then((data)=>{
                console.log(data);
                
            })




        }
    )
    });
    
    

}

window.addEventListener(
    'load',
    () => {
        setInterval(
            fetch_new_posts,  
            5000)           
    }
)

window.addEventListener(
    'load',
    edit_text     
    
)