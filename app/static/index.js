const api_url = '/api/';

let mtypes = []
let selected_mtype = []

//                                      API CRUD first layer
class Api {
    static fetch(object_url) {
        return fetch(api_url+object_url, {method: 'get'}).then(res => res.json())
    }

    static create(object_url, object) {
        return fetch(api_url+object_url, {
            method: 'post',
            body: JSON.stringify(object),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then( res => res.json() )
    }

    static update(object_url, object) {
        return fetch(api_url+object_url, {
            method: 'put',
            body: JSON.stringify(object),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then( res => res.json() )
    }

    static delete(object_url) {
        return fetch(api_url+object_url, {method: 'delete'}).then(res => res.json())
    }

}






function show_tree (){
    const $tree_place = document.querySelector('#tree')
    function render_tree(object, place){
        const chain = new Promise((resolve, reject)=>{
            let ins = `<li id = "${object.id}" class = "${object.info.kind}"><span onclick="tree_listener()">${object.name}</span><ul id ="${object.info.kind+object.id}"></ul></li>`
            place.insertAdjacentHTML("beforeend", ins)
            $tree_spiner = document.querySelector('#tree_spiner')
            resolve()        
        })
        chain.then((result)=>{
            if(object.subs){object.subs.map(id=>{ Api.fetch(object.info.content+'/'+id).then( (res)=>{render_tree(res, document.querySelector(`#${object.info.kind+object.id}`))} ) })}
        })
    }
    $tree_place.innerHTML = ''
    Api.fetch('metatypes').then(backendMtypes => {
        backendMtypes.map( (el)=>{render_tree(el, $tree_place) })
    })
}






function createMtype() {
    const nameField = document.querySelector('#itemName')
    if(nameField.value == ''){alert('Имя не должно быть пустым')}
    else{
            const newMtype = {
                name: nameField.value
            }
        
            Api.create('metatypes', newMtype).then( () => {
                alert('Новый метатэг сохранен!')
                show_tree()
                nameField.value = ''
            })    
        }
}

const render_editor_mtype = (selected_obj) => {
    switch (selected_obj.info.kind) {
        case 'metatypes': 
            document.querySelector('#editorheader').innerHTML = 'Редактирование   <div class="bold">М Е Т А Т Э Г А</div>';
            break;

        case 'types': 
            document.querySelector('#editorheader').innerHTML = 'Редактирование   <div class="bold">Т Э Г А</div>';
            break;  
            
        case 'topics': 
            document.querySelector('#editorheader').innerHTML = 'Редактирование   <div class="bold"> Т Е М Ы</div>';
            break;    
    }

    document.querySelector('#editor').innerHTML = `
    <div class="form-group">
    <label for="itemName">Имя</label>
    <input type="text" class="form-control" id="itemName" value="${selected_obj.name}">
    <br>
    <button type="button" class="btn btn-success btn-sm" id = "saveMtype">Сохранить метатэг</button>
    </div>
    `
    document.querySelector('#saveMtype').addEventListener('click', createMtype)
}

function tree_listener() {
    Api.fetch(event.target.parentNode.className+'/'+event.target.parentNode.id).then( (opened)=>{
        render_editor_mtype(opened)
    })
}

document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#newmtype').addEventListener('click', ()=>{ render_editor_mtype() })
    show_tree()
   
})


