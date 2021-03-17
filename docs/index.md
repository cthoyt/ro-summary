---
layout: home
---
Summary of the Relation Ontology. There are {{ site.data.summary.total }}
total relationships as of {{ site.data.summary.total }}.

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
        <td><a href="https://www.ebi.ac.uk/ols/ontologies/ro/properties?iri=http://purl.obolibrary.org/obo/{{ entry.ro }}">{{ entry.ro }}</a></td>
        <td align="right">{{ entry.count }}</td>
    </tr>
{% endfor %}
</tbody>
</table>
