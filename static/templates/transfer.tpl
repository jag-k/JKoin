<br/>
<br/>
<form method="get" action="/transfer">
    <div class="form-group">
        <div class="input-group">
            <input name="from" type="text" placeholder="Enter From VKID transfer" class="form-control">
            <input name="to" type="text" placeholder="Enter To VKID transfer" class="form-control">
            <input name="count" type="numb" pattern="^[0-9]+$" placeholder="Enter count transfer JKoin" class="form-control">
            <div class="input-group-append">
                <button class="btn btn-secondary" type="submit">Submite</button>
            </div>
        </div>
    </div>
</form>

%if res and res['from'] and res['to']:
<br/>
<br/>

<p>From <a href="https://vk.com/id{{res['from']['user']['id']}}">{{res['from']['user']["first_name"] + " " + res['from']['user']["last_name"]}}</a> (<strong><abbr title="Balance">{{ res['from']['balance'] }}</abbr></strong>) to <a href="https://vk.com/id{{res['to']['user']['id']}}">{{res['to']['user']["first_name"] + " " + res['to']['user']["last_name"]}}</a> (<strong><abbr title="Balance">{{ res['to']['balance'] }}</abbr></strong>) {{res['transfer']}} <a href="/">JKoins</a> were transferred</p>

%elif res:
<br/>
<br/>

<p>IDs is incorrect! Please, try again.</p>
%end