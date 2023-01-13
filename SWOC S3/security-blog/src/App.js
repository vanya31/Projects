import React from "react";
import "./App.css";

import Posts from "./components/Posts/Posts";
import Dashboard from "./components/Dashboard/Dashboard";
import { BrowserRouter, Route, Switch } from 'react-router-dom';




const App = () => {
return (
	<div className="main-container">
	<h1 className="main-heading">
		Technical Blog
	</h1>
	<Posts />
	</div>
);
};

export default App;
