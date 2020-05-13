
const form = document.getElementById('addUser');
form.addEventListener('submit', myfunct)
function myfunct(e) {
    console.log(document.querySelector('#hastag'));
    e.preventDefault();
    const hastag = document.getElementById('hastag').value;
    const comment = document.getElementById('content').value;
    urll = '{% url "crud_ajax_create" %}?hastag=' + hastag + '&content=' + comment;
    document.getElementById('hastag').value = '';
    document.getElementById('content').value = '';
    const req = new XMLHttpRequest;
    req.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            const values = eval(req.responseText);
            for (let i = 0; i < values.length; i++) {
                addUser(values[i])
            }
        }
    };
    req.open("GET", urll, true);
    req.send();
}
function addUser(post) {
    const list = document.querySelector('#showDivv');
    const row = document.createElement('div');
    row.innerHTML = `
      <div class="card m-2" style="width: 18rem;">
      <div class="card-body">
        <h5 class="card-title">${post.user}</h5>
        <h6 class="card-subtitle mb-2 text-muted">${post.hastag}</h6>
        <p class="card-text">${post.content}</p>
        <hr>
        ${post.like}
        <hr>
        <form action="../liked/${post.id}/" method="POST">
          {% csrf_token %}
          <button class="btn btn-success" type="submit">Like</button>
        </form>
        <a href="../delete/${post.id}/" class="card-link"><i class="fas fa-trash-alt"></i></a>
        <a href="#" data-toggle="modal" data-target="#exampleModal" class="ml-3">
          <i class="fas fa-pencil-alt"></i>
        </a>
      </div>
    </div>          
      `
    list.appendChild(row);
}