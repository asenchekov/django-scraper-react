import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import axios from 'axios';


const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get(`${window.location.href}api/items`)
      .then((res) => setData(res.data));
  }, []);

  const sortByHandler = (sortBy) => {
    axios.get(`${window.location.href}api/items?sortby=${sortBy}`)
      .then((res) => setData(res.data));
    console.log(sortBy);
  }

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
    <div className="table-wrapper">
      <h2>ITEMS</h2>
      <table className="fl-table">
        <thead>
          <tr>
            <th>
              <button
                onClick={() => sortByHandler('id')}>ID
              </button>
            </th>
            <th>
              <button
                onClick={() => sortByHandler('url')}>URL
              </button>
            </th>
            <th>
              <button
                onClick={() => sortByHandler('name')}>NAME
              </button>
            </th>
            <th>
              <button
                onClick={() => sortByHandler('price')}>PRICE
              </button>
            </th>
            <th>
              <button
                onClick={() => sortByHandler('sku')}>SKU
              </button>
            </th>
            <th>
              <button
                onClick={() => sortByHandler('description')}>DESCRIPTION
              </button>
            </th>
          </tr>
        </thead>
        <tbody>
          {items}
        </tbody>
      </table>
    </div>
  );

  return data && table;
};

ReactDOM.render(<App />, document.getElementById("app"));
