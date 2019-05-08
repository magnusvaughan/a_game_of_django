// App.js
import React, { Component } from 'react';

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
    return (
      <div>
        {this.state.characters.map(item => (
          <div key={item.id}>
            <h1>{item.name}</h1>
            <span>{item.culture}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
