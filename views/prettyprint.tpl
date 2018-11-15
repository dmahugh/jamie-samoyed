% rebase('layout.tpl', title='API response')
% import json
% json_data = json.loads(pprint_json)

<h2>API response &mdash; {{ api_route }}</h2>

<pre>{{! pprint_json }}</pre>

% if 'filename' in json_data:
<img src="{{ json_data['filename'] }}" />
% end
