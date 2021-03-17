---
layout: home
---
Summary of the Relation Ontology. There are {{ site.data.summary.total }}
total relationships as of {{ site.data.summary.date }}. Download this data
from [here](https://github.com/cthoyt/ro-summary/raw/main/docs/_data/summary.tsv).
This table is created by open source code at
<a href="https://github.com/cthoyt/ro-summary"><img src="github-ocon.svg"/> cthoyt/ro-summary</a>.

<table>
<thead>
<tr>
    <th>WD ID</th>
    <th>Label</th>
    <th>RO ID</th>
    <th>Count</th>
</tr>
</thead>
<tbody>
{% for entry in site.data.summary.rows %}
    <tr>
        <td><a href="https://www.wikidata.org/wiki/Property:{{ entry.wd }}">{{ entry.wd }}</a></td>
        <td>{{ entry.label }}</td>
        <td>
            <a href="https://www.ebi.ac.uk/ols/ontologies/ro/properties?iri=http://purl.obolibrary.org/obo/{{ entry.ro }}">
                {{ entry.ro }}
            </a>
        </td>
        <td align="right">{{ entry.count }}</td>
    </tr>
{% endfor %}
</tbody>
</table>
