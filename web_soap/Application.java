import javax.xml.ws.Endpoint;

public class Application {
    public static void main(String[] args) {
        System.out.println("debut du deploiement de mon service");
        String url = "http://localhost:8888/";
        Endpoint.publish(url, new Monservice());
        System.out.println("le service web est deployer");
    }
}