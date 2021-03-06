---
layout: home
---
There are {{ site.data.summary.total }} triples in Wikidata annotated with relations
from the Relation Ontology (retrieved on {{ site.data.summary.date }}).
Download the summary from [here](https://github.com/cthoyt/ro-summary/raw/main/summary.tsv).
Download the mappings as [SSSOM](https://github.com/mapping-commons/SSSOM) from
[here](https://github.com/cthoyt/ro-summary/raw/main/sssom.tsv).
Generated by <a href="https://github.com/cthoyt/ro-summary">
<img src="github-icon.svg" height="16" />&nbsp;cthoyt/ro-summary</a>.

<table>
<thead>
<tr>
    <th>WD ID</th>
    <th>WD Label</th>
    <th>RO ID</th>
    <th>RO Label</th>
    <th>Count</th>
    <th>Sample</th>
</tr>
</thead>
<tbody>
{% for entry in site.data.summary.rows %}
    <tr>
        <td><a href="https://www.wikidata.org/wiki/Property:{{ entry.wd }}">{{ entry.wd }}</a></td>
        <td>{{ entry.wd_label }}</td>
        <td>
            <a href="https://www.ebi.ac.uk/ols/ontologies/ro/properties?iri=http://purl.obolibrary.org/obo/{{ entry.ro }}">
                {{ entry.ro }}
            </a>
        </td>
        <td>{{ entry.ro_label }}</td>
        <td align="right">{{ entry.count }}</td>
        <td><a href="https://query.wikidata.org/#SELECT%20%3Fsubject%20%3FsubjectLabel%20%3Fobject%20%3FobjectLabel%20%0AWHERE%20%0A%7B%0A%20%20%3Fsubject%20wdt%3A{{ entry.wd }}%20%3Fobject.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D%0ALIMIT%2010">Sample</a></td>
    </tr>
{% endfor %}
</tbody>
</table>
