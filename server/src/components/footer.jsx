export default function Footer()
{
    return (
        <div className="footer">
            <div className="container">
                <div className="row">
                    <div className="col-md-6">
                        <p>&copy; 2020 DBC</p>
                    </div>
                    <div className="col-md-6">
                        <ul className="list-inline">
                            <li className="list-inline-item">
                                <a href="/">Home</a>
                            </li>
                            <li className="list-inline-item">
                                <a href="/about/">About</a>
                            </li>
                            <li className="list-inline-item">
                                <a href="/contact/">Contact</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
}
