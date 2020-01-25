import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import axios from 'axios';


const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/items')
      .then((res) => setData(res.data));
  }, []);

  let items;

  if (data) {
    items = data.map((item) => (
      <tr key={item.id}>
        <td>{item.id}</td>
        <td>{item.url}</td>
        <td>{item.name}</td>
        <td>{item.price}</td>
        <td>{item.sku}</td>
        <td>{item.description}</td>
      </tr>
    ));
  }

  const table = (
    <table>
      <caption>ITEMS</caption>
      <tbody>
        <tr>
          <th>id</th>
          <th>url</th>
          <th>name</th>
          <th>price</th>
          <th>sku</th>
          <th>description</th>
        </tr>
        {items}
      </tbody>
    </table>
  );

  return data ? table : <h1>LOADING</h1>
};

ReactDOM.render(<App />, document.getElementById("app"));
