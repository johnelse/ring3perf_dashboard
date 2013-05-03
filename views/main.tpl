<html>
  <head>
    <title>Ring3 performance issues</title>
  </head>
  <body>
    <h1>Ring3 Performance Dashboard</h1>
    <table border="1" width="100%">
%for group in groups:
      <tr>
        <td colspan="3">
          <a href="{{url}}/browse/{{group.key}}">{{group.key}}</a> - {{group.fields.summary}}
        </td>
      <tr>
%  for link in group.fields.issuelinks:
%    issue = link.outwardIssue
      <tr>
        <td>
          <a href="{{url}}/browse/{{issue.key}}">{{issue.key}}</a>
        </td>
        <td>
          {{issue.fields.summary}}
        </td>
        <td>
          {{issue.fields.status.name}}
        </td>
      </tr>
%  end
%end
    </table>
  </body>
</html>
