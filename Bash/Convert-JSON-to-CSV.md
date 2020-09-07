# Convert JSON to CSV with jq

With a input json like this:

	// file.json
	[
		{
			"type": "Event1",
			"time": 20
		},
		{
			"type": "Event2",
			"distance": 100
		}
	]

Use this onliner to convert it to csv:

	cat file.json | jq -r '(map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv' > file.csv

It gives the following output:

	"distance","time","type"
	,20,"Event1"
	100,,"Event2"
