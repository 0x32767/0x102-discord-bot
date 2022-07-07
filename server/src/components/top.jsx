import { Outlet } from "react-router-dom";


export default function PageTop(tab)
{
    return (
        <>
            <nav className="navbar navbar-expand-lg navbar-light bg-light" style={{"paddingLeft": "1rem"}}>
                <a className="navbar-brand" href="/about/">DBC</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item active" key={"1"}>
                            <a className="nav-link" href="/home/">Home {tab === "home" ? (<span className="sr-only">&#40current&#41</span>): ''}</a>
                        </li>
                        <li className="nav-item" key={"2"}>
                            <a href="/" className="nav-link">bots{tab === "bots" ? (<span className="sr-only">&#40current&#41</span>): ''}</a>
                        </li>
                        <li className="nav-item" key={"3"}>
                            <a href="/about/" className="nav-link">about {tab === "about" ? (<span className="sr-only">&#40current&#41</span>): ''}</a>
                        </li>
                    </ul>
                    <form className="form-inline my-2 my-lg-0">
                        <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"/>
                    </form>
                </div>
            </nav>
            <Outlet/>
        </>
    );
}
