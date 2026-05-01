
// SOAP : Simple Object Access Protocol
//JAX-WS (java annotation XML for Wrb Service)
//JAXB (Java Architecture XML Building)
//URL :Uniforme Resource Locator
//URN: uniforme Ressource Name
//URI: uniforme Ressource Identifier
//URN + URL = URI
import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

@WebService(targetNamespace = "http://www.polytech.fr")
public class Monservice {
    @WebMethod(operationName = "convertir")
    public double conversion(double mt) {
        return mt * 0.9;
    }

    public double somme(@WebParam(name = "parametre1") double a, double b) {
        return a + b;
    }

    public Etudiant getEtudiant(int identifiant) {
        return new Etudiant(identifiant, "mario", 19);
    }
}