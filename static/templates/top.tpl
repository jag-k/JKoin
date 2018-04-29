<br/>
<br/>

%if top:
<h2>TOP {{ count }}:</h2>
%count = 0
<table class="table">
  <thead class="thead-dark">
    <tr>
      <th scope="col">#</th>
      <th scope="col">User</th>
      <th scope="col">Total</th>
    </tr>
  </thead>
  <tbody>
    %for i in top:
      %count += 1
      <tr>
          <th scope="row">{{ count }}</th>
          <td><a href="https://vk.com/id{{i['user']['id']}}">{{i['user']["first_name"] + " " + i['user']["last_name"]}}</a></td>
          <td>{{ i['count'] }}</td>
      </tr>
    %end
  </tbody>
</table>
<br/>
<br/>

%else:
<h1>No one is here... Come back later)</h1>
