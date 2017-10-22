<?php

require("phpsqlajax_dbinfo.php");

// Start XML file, create parent node

$dom = new DOMDocument("1.0");
$node = $dom->createElement("markers");
$parnode = $dom->appendChild($node);

// Opens a connection to a MySQL server

class MyDB extends SQLite3
{
    function __construct()
    {
        $this->open('db.sqlite3');
    }
}

// Set the active MySQL database

$$db = new MyDB();

// Select all the rows in the markers table

$result = $db->query("SELECT * FROM CityApp_cityinfo WHERE 1"


header("Content-type: text/xml");

// Iterate through the rows, adding XML nodes for each

while ($row = @fetchArray($result)){
  // Add to XML document node
  $node = $dom->createElement("marker");
  $newnode = $parnode->appendChild($node);
  $newnode->setAttribute("id",$row['id']);
  $newnode->setAttribute("name",$row['name']);
  $newnode->setAttribute("address", $row['address']);
  $newnode->setAttribute("lat", $row['lat']);
  $newnode->setAttribute("lng", $row['lng']);
  $newnode->setAttribute("type", $row['type']);
}

echo $dom->saveXML();

?>