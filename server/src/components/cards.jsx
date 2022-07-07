function MaintainedDIV(params)
{
    return (
        <div className="btn btn-success ms-1">
            This bot is maintained by <b>{params.author}</b>
        </div>
    );
}


function DiscontinuedDIV()
{
    return (
        <div className="btn btn-danger ms-1 disabled" style={{opacity: "1"}}>
            This bot is discontinued
        </div>
    );
}

function Card(params)
{
    console.log(params);
    return (
        <div className="card" key={params.info.id}>
            <div className="card-body">
                <h5 className="card-title">{params.info.title}</h5>
                <p className="card-text">{params.info.text}</p>
                <div style={{whiteSpace: "nowrap", overflowX: "auto"}}>
                    <a style={{display: "inline-block"}} href={params.info.id} className="btn btn-primary">Go somewhere</a>
                    <div style={{display: "inline-block"}}>{params.info.maintained ? <MaintainedDIV author={params.info.author}/> : <DiscontinuedDIV/>}</div>
                </div>
            </div>
        </div>
    );
}


export default function CardArray()
{
    return (
        <div itemID="cards" key="cards">
            {[
                {id: 0, repo: "", author: "0x32", title: "0x102", text: "A general purpose discord bot.", maintained: true},
                {id: 1, repo: "", author: "tester", title: "test", text: "a test", maintained: false},
            ].map((card) => <Card info={card} key={card.id.toString()}/>)}
        </div>
    )
}
