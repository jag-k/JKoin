<br/>

<h2>Rule:</h2>
<p>The string should look like: <strong>VKID-string</strong> , where <mark>VKID</mark> is the id or domain <a href="https://vk.com/">vk.com</a>, and <mark>string</mark> a string of any length</p>
<p>MD5-hash must start with {{ coef }} characters of the <mark>VKID</mark> MD5-hash</p>

<pre><code>
string: 1-tUddOyxWhm
    id = 1
    string = tUddOyxWhm
    MD5(id)[:4] == MD5(string)[:4] == "c4ca"

string: id1-OdKmnRPbNr
    id = "id1"
    string = OdKmnRPbNr
    MD5(id)[:4] == MD5(string)[:4] == "fafe"

string: durov-vhOSROTXBv
    id = "durov"
    string = vhOSROTXBv
    MD5(id)[:4] == MD5(string)[:4] == "4d6b"
</code></pre>

<br/>

<form method="get" action="/">
    <div class="form-group">
        <label for="exampleFormControlTextarea1">Enter Strings:</label>
        <textarea class="form-control" name="hashes" id="exampleFormControlTextarea1" cols="80" rows="10" placeholder="Enter strings in this textbox">{{ ph }}</textarea>
    </div>
    <br/>
    <button type="submit" class="btn btn-secondary">Submit</button>
</form>


%if hashes:
%count = 0

<br/>
<br/>

<h2>Hashes:</h2>
<table class="table">
  <thead class="thead-dark">
    <tr>
      <th scope="col">#</th>
      <th scope="col">Hash</th>
      <th scope="col">User</th>
      <th scope="col">Status</th>
    </tr>
  </thead>
  <tbody>
    %for i in hashes:
        %count += 1
        <tr>
          <th scope="row">{{ count }}</th>
          <td>{{i}}</td>
            % user = hashes[i]["user"]
            % if user:
                <td><a href="https://vk.com/id{{user['id']}}">{{user["first_name"] + " " + user["last_name"]}}</a></td>
            %else:
                <td>None</td>
            %end
          <td>{{("OK" if hashes[i]["status"] else "Error") if type(hashes[i]['status']) == bool else hashes[i]['status']}}</td>
        </tr>
    %end
  </tbody>
</table>
<li>OK — OK</li>
<li>Error — String is incorrect</li>
<li>IDB — String is correct, but it's in DataBase</li>
<br/>
<br/>
