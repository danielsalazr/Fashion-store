import React, { Component } from 'react'
import "@components/Header"
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Header from '../components/Header';
import Main from '../components/Main';

const App = () => {
    return (
        
        <div>
            <Header />
            <Main />
        </div>
    );
}

export default App;