import CardArray from "../components/cards";
import PageTop from "../components/top";
import Footer from "../components/footer";


function Index()
{
    return (
        <div>
            <PageTop tab={'bots'}/>
            <br/>
            <CardArray/>
            <br/>
            <Footer/>
        </div>
    );
}


export default Index;
