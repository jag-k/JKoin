<br/>
<br/>
<form method="get" action="/wallet">
    <div class="form-group">
        <div class="input-group mb-3">
            <input name="id" type="text" class="form-control" placeholder="Enter Your VKID" aria-label="Recipient's username" aria-describedby="basic-addon2">
            <div class="input-group-append">
                <button class="btn btn-secondary" type="submit">Submite</button>
            </div>
        </div>
    </div>
</form>

%if count and count["user"]:
    <p><a href="https://vk.com/id{{count['user']['id']}}">Your</a> store: {{ count['count'] }}</p>
%elif count['count'] != -1:
    <p>Your VKID is incorrect. Please try again</p>
