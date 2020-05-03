const mtype_url = '/api/metatypes';

let mtypes = []



const show_mtype = mtype => {
    return `
    <li>${mtype.name}</li>
    `
}

const render_editor_mtype = () => {
    document.querySelector('#editorheader').innerHTML = 'Создание нового метатэга'
    document.querySelector('#editor').innerHTML = `
    <div class="form-group">
    <label for="itemName">Имя</label>
    <input type="text" class="form-control" id="itemName" value="">
    <br>
    <button type="button" class="btn btn-success btn-sm" id = "saveMtype">Сохранить метатэг</button>
    </div>
    `
    document.querySelector('#saveMtype').addEventListener('click', createMtype)
}

class MtypeApi {
    static fetch() {
        return fetch(mtype_url, {method: 'get'}).then(res => res.json())
    }

    static create(Mtype) {
        return fetch(mtype_url, {
            method: 'post',
            body: JSON.stringify(Mtype),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then( ()=>{
            
        } )

    }
}



function renderMtypes(_mtypes = []) {
    const $mtypes = document.querySelector('#tree')

    if (_mtypes.length > 0) {
        $mtypes.innerHTML = _mtypes.map(elem => show_mtype(elem)).join(' ')

    } else {
        $mtypes.innerHTML = '<div>Пока нет метатэгов</div>'
    }
}

function createMtype() {
    const nameField = document.querySelector('#itemName')
    if(nameField.value == ''){alert('Имя не должно быть пустым')}
    else{
        const newMtype = {
            name: nameField.value
        }
    MtypeApi.create(newMtype).then( () => {alert('Saved!')})    
    }
}


document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#newmtype').addEventListener('click', render_editor_mtype)
    MtypeApi.fetch().then(backendMtypes => {
        mtypes = backendMtypes.concat()
        renderMtypes(mtypes)
    })
})


