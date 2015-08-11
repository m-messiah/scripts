#!/bin/bash

cat << END
<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Upstream response time', '$1'],
END

# Check if $upstream_response_time in correct place
# Purpose log line: $addr\t$status\t$method\t$uri\t$upstream_response_time
# So, delimeter is '\t' and variable is $5
cat $1 | awk -F '\t' '{printf "%.1f\n", $15;}' | sort -n | uniq -c | awk '{printf "\t[\"%s\", %s],\n", $2, log($1);}'

cat << END2
    ]);
        var options = {
          title: 'Upstream response time',
          hAxis: {title: 'Time'},
          vAxis: {minValue: 0}
        };

        var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 1000px; height: 700px;"></div>
  </body>
</html>
END2
