import java.io.Serializable;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class Etudiant implements Serializable {
    private int indentifiant;
    private String nom;
    private double moyenne;

    public Etudiant() {
    }

    public Etudiant(int identifiant, String nom, double moyenne) {
        this.indentifiant = identifiant;
        this.nom = nom;
        this.moyenne = moyenne;
    }

    public int getIdentifiant() {
        return this.indentifiant;
    }

    public String getNom() {
        return this.nom;
    }

    public double getMoyenne() {
        return this.moyenne;
    }

    public void setIdentifiant(int id) {
        this.indentifiant = id;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setMoyenne(double moyenne) {
        this.moyenne = moyenne;
    }
}