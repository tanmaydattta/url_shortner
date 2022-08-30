import { useEffect, useState } from "react";
import InfoTable from "./components/info_tables";
import './index.css';
function App() {
    const [longurl, setLongurl] = useState("");
    const [shorturl, setShorturl] = useState("");
    const [returnLongURL, setReturnLongURL] = useState("");
    const [returnClicks, setReturnClicks] = useState("-");
    const [obj, setInfoTable] =useState([{}]);
    const getInfo = async ()=>{
        // fetch updated table
        fetch("http://localhost:8000/summary/", {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        })
            .then((res) => res.json())
            .then((data) => {
            setInfoTable(data);
            });
    };

    useEffect(()=>{
    getInfo();
    },[]);

    const handleSubmit = (e) => {
        e.preventDefault();

        fetch("http://localhost:8000/shorten/", {
            method: "POST",
            body: JSON.stringify({ longurl: longurl }),
            headers: { "Content-Type": "application/json" },
        })
            .then((res) => res.json())
            .then((data) => {
                setShorturl(data.shorturl);
                setReturnLongURL(data.longurl);
                setReturnClicks(data.clicks);
                setLongurl("");
            });
    };

    const handleRedirectReuqest =  ()=> {
        fetch("http://localhost:8000/clicked/", {
            method: "POST",
            body: JSON.stringify({ shorturl: shorturl }),
            headers: { "Content-Type": "application/json" },
        })
            .then((res) => res.json())
            .then((data) => {
                setReturnClicks(data.clicks);
            })
        // fetch updated table
        .then(()=>fetch("http://localhost:8000/summary/", {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        })
            .then((res) => res.json())
            .then((data) => {
            setInfoTable(data);
            })
            );
            window.open(returnLongURL);

    }
    // render the app
    return (
      <div>
        <div className="header">

          Url shortner app
        </div>
        <div className="body">
            <input
                style={{ padding:"10px 10px 1px  2px", margin:"20px 10px 10px 2px" }}
                width="400px"
                type="text"
                name="longurl"
                value={longurl}
                onChange={(e) => setLongurl(e.target.value)}
            />
            <button
                style={{textAligh: "center"}}
                type="submit"
                onClick={(e) => handleSubmit(e)}
                disabled={!longurl}
            >
                shorten
            </button>

            <div>
                <p>Long URL: {returnLongURL}</p>
                <p
                    style={{ cursor: "pointer" }}
                    onClick= {()=>handleRedirectReuqest()}
                >
                    Short URL: {shorturl}
                </p>
            </div>
            <div> clicked: {returnClicks}</div>
        </div>
        <InfoTable data="test" tableInfo={obj}></InfoTable>
      </div>
    );
}

export default App;