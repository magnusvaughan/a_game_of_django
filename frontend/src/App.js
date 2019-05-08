// App.js
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import 'react-bootstrap-table2-filter/dist/react-bootstrap-table2-filter.min.css'; 
import React, { Component } from 'react';
import BootstrapTable from 'react-bootstrap-table-next';
import filterFactory, { textFilter } from 'react-bootstrap-table2-filter';

class App extends Component {
  state = {
    characters: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/characters');
      const characters = await res.json();
      this.setState({
        characters
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {

    const characters = this.state.characters;

    const columns = [
    {
      dataField: 'name',
      text: 'Name',
      sort: true,
      filter: textFilter()
    },
    {
      dataField: 'sex',
      text: 'Sex'
    },
    {
      dataField: 'culture',
      text: 'titles'
    },
    {
      dataField: 'aliases',
      text: 'Aliases'
    },
    {
      dataField: 'born',
      text: 'Born'
    },
    {
      dataField: 'died',
      text: 'Died'
    },
    {
      dataField: 'father',
      text: 'Father'
    },
    {
      dataField: 'mother',
      text: 'Mother'
    },
    {
      dataField: 'spouse',
      text: 'Spouse'
    },
    {
      dataField: 'children',
      text: 'Children'
    },
    {
      dataField: 'allegiances',
      text: 'Allegiances'
    },
    {
      dataField: 'books',
      text: 'Books'
    },
    {
      dataField: 'pov_books',
      text: 'POV Books'
    },
    {
      dataField: 'played_by',
      text: 'Played by'
    },
    {
      dataField: 'tv_series',
      text: 'TV Series'
    }];
    return (
      <BootstrapTable keyField='id' data={ characters } columns={ columns } filter={ filterFactory() }/>
    )
  }
}

export default App;
