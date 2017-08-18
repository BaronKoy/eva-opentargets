//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.8-b130911.1802 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2017.08.17 at 04:29:30 PM BST 
//


package uk.ac.ebi.eva.clinvar.model.v47;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlSchemaType;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for TraitSetType complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType name="TraitSetType">
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element name="Trait" type="{}TraitType" maxOccurs="unbounded"/>
 *         &lt;element name="Name" type="{}SetElementSetType" maxOccurs="unbounded" minOccurs="0"/>
 *         &lt;element name="Symbol" type="{}SetElementSetType" maxOccurs="unbounded" minOccurs="0"/>
 *         &lt;element name="AttributeSet" maxOccurs="unbounded" minOccurs="0">
 *           &lt;complexType>
 *             &lt;complexContent>
 *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                 &lt;sequence>
 *                   &lt;element name="Attribute">
 *                     &lt;complexType>
 *                       &lt;simpleContent>
 *                         &lt;extension base="&lt;>AttributeType">
 *                           &lt;attribute name="Type" use="required" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                         &lt;/extension>
 *                       &lt;/simpleContent>
 *                     &lt;/complexType>
 *                   &lt;/element>
 *                   &lt;element name="Citation" type="{}CitationType" maxOccurs="unbounded" minOccurs="0"/>
 *                   &lt;element name="XRef" type="{}XrefType" maxOccurs="unbounded" minOccurs="0"/>
 *                   &lt;element name="Comment" type="{}CommentType" maxOccurs="unbounded" minOccurs="0"/>
 *                 &lt;/sequence>
 *               &lt;/restriction>
 *             &lt;/complexContent>
 *           &lt;/complexType>
 *         &lt;/element>
 *         &lt;element name="Citation" type="{}CitationType" maxOccurs="unbounded" minOccurs="0"/>
 *         &lt;element name="XRef" type="{}XrefType" maxOccurs="unbounded" minOccurs="0"/>
 *         &lt;element name="Comment" type="{}CommentType" maxOccurs="unbounded" minOccurs="0"/>
 *       &lt;/sequence>
 *       &lt;attGroup ref="{}CVIdentifiers"/>
 *       &lt;attribute name="Type" use="required">
 *         &lt;simpleType>
 *           &lt;restriction base="{http://www.w3.org/2001/XMLSchema}string">
 *             &lt;enumeration value="Disease"/>
 *             &lt;enumeration value="DrugResponse"/>
 *             &lt;enumeration value="Finding"/>
 *             &lt;enumeration value="PhenotypeInstruction"/>
 *             &lt;enumeration value="TraitChoice"/>
 *           &lt;/restriction>
 *         &lt;/simpleType>
 *       &lt;/attribute>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "TraitSetType", propOrder = {
    "trait",
    "name",
    "symbol",
    "attributeSet",
    "citation",
    "xRef",
    "comment"
})
public class TraitSetType {

    @XmlElement(name = "Trait", required = true)
    protected List<TraitType> trait;
    @XmlElement(name = "Name")
    protected List<SetElementSetType> name;
    @XmlElement(name = "Symbol")
    protected List<SetElementSetType> symbol;
    @XmlElement(name = "AttributeSet")
    protected List<TraitSetType.AttributeSet> attributeSet;
    @XmlElement(name = "Citation")
    protected List<CitationType> citation;
    @XmlElement(name = "XRef")
    protected List<XrefType> xRef;
    @XmlElement(name = "Comment")
    protected List<CommentType> comment;
    @XmlAttribute(name = "Type", required = true)
    protected String type;
    @XmlAttribute(name = "ID")
    @XmlSchemaType(name = "positiveInteger")
    protected BigInteger id;

    /**
     * Gets the value of the trait property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the trait property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getTrait().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link TraitType }
     * 
     * 
     */
    public List<TraitType> getTrait() {
        if (trait == null) {
            trait = new ArrayList<TraitType>();
        }
        return this.trait;
    }

    /**
     * Gets the value of the name property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the name property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getName().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link SetElementSetType }
     * 
     * 
     */
    public List<SetElementSetType> getName() {
        if (name == null) {
            name = new ArrayList<SetElementSetType>();
        }
        return this.name;
    }

    /**
     * Gets the value of the symbol property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the symbol property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getSymbol().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link SetElementSetType }
     * 
     * 
     */
    public List<SetElementSetType> getSymbol() {
        if (symbol == null) {
            symbol = new ArrayList<SetElementSetType>();
        }
        return this.symbol;
    }

    /**
     * Gets the value of the attributeSet property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the attributeSet property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getAttributeSet().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link TraitSetType.AttributeSet }
     * 
     * 
     */
    public List<TraitSetType.AttributeSet> getAttributeSet() {
        if (attributeSet == null) {
            attributeSet = new ArrayList<TraitSetType.AttributeSet>();
        }
        return this.attributeSet;
    }

    /**
     * Gets the value of the citation property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the citation property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getCitation().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link CitationType }
     * 
     * 
     */
    public List<CitationType> getCitation() {
        if (citation == null) {
            citation = new ArrayList<CitationType>();
        }
        return this.citation;
    }

    /**
     * Gets the value of the xRef property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the xRef property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getXRef().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link XrefType }
     * 
     * 
     */
    public List<XrefType> getXRef() {
        if (xRef == null) {
            xRef = new ArrayList<XrefType>();
        }
        return this.xRef;
    }

    /**
     * Gets the value of the comment property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the comment property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getComment().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link CommentType }
     * 
     * 
     */
    public List<CommentType> getComment() {
        if (comment == null) {
            comment = new ArrayList<CommentType>();
        }
        return this.comment;
    }

    /**
     * Gets the value of the type property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getType() {
        return type;
    }

    /**
     * Sets the value of the type property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setType(String value) {
        this.type = value;
    }

    /**
     * Gets the value of the id property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getID() {
        return id;
    }

    /**
     * Sets the value of the id property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setID(BigInteger value) {
        this.id = value;
    }


    /**
     * <p>Java class for anonymous complex type.
     * 
     * <p>The following schema fragment specifies the expected content contained within this class.
     * 
     * <pre>
     * &lt;complexType>
     *   &lt;complexContent>
     *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *       &lt;sequence>
     *         &lt;element name="Attribute">
     *           &lt;complexType>
     *             &lt;simpleContent>
     *               &lt;extension base="&lt;>AttributeType">
     *                 &lt;attribute name="Type" use="required" type="{http://www.w3.org/2001/XMLSchema}string" />
     *               &lt;/extension>
     *             &lt;/simpleContent>
     *           &lt;/complexType>
     *         &lt;/element>
     *         &lt;element name="Citation" type="{}CitationType" maxOccurs="unbounded" minOccurs="0"/>
     *         &lt;element name="XRef" type="{}XrefType" maxOccurs="unbounded" minOccurs="0"/>
     *         &lt;element name="Comment" type="{}CommentType" maxOccurs="unbounded" minOccurs="0"/>
     *       &lt;/sequence>
     *     &lt;/restriction>
     *   &lt;/complexContent>
     * &lt;/complexType>
     * </pre>
     * 
     * 
     */
    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlType(name = "", propOrder = {
        "attribute",
        "citation",
        "xRef",
        "comment"
    })
    public static class AttributeSet {

        @XmlElement(name = "Attribute", required = true)
        protected TraitSetType.AttributeSet.Attribute attribute;
        @XmlElement(name = "Citation")
        protected List<CitationType> citation;
        @XmlElement(name = "XRef")
        protected List<XrefType> xRef;
        @XmlElement(name = "Comment")
        protected List<CommentType> comment;

        /**
         * Gets the value of the attribute property.
         * 
         * @return
         *     possible object is
         *     {@link TraitSetType.AttributeSet.Attribute }
         *     
         */
        public TraitSetType.AttributeSet.Attribute getAttribute() {
            return attribute;
        }

        /**
         * Sets the value of the attribute property.
         * 
         * @param value
         *     allowed object is
         *     {@link TraitSetType.AttributeSet.Attribute }
         *     
         */
        public void setAttribute(TraitSetType.AttributeSet.Attribute value) {
            this.attribute = value;
        }

        /**
         * Gets the value of the citation property.
         * 
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the citation property.
         * 
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getCitation().add(newItem);
         * </pre>
         * 
         * 
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link CitationType }
         * 
         * 
         */
        public List<CitationType> getCitation() {
            if (citation == null) {
                citation = new ArrayList<CitationType>();
            }
            return this.citation;
        }

        /**
         * Gets the value of the xRef property.
         * 
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the xRef property.
         * 
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getXRef().add(newItem);
         * </pre>
         * 
         * 
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link XrefType }
         * 
         * 
         */
        public List<XrefType> getXRef() {
            if (xRef == null) {
                xRef = new ArrayList<XrefType>();
            }
            return this.xRef;
        }

        /**
         * Gets the value of the comment property.
         * 
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the comment property.
         * 
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getComment().add(newItem);
         * </pre>
         * 
         * 
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link CommentType }
         * 
         * 
         */
        public List<CommentType> getComment() {
            if (comment == null) {
                comment = new ArrayList<CommentType>();
            }
            return this.comment;
        }


        /**
         * <p>Java class for anonymous complex type.
         * 
         * <p>The following schema fragment specifies the expected content contained within this class.
         * 
         * <pre>
         * &lt;complexType>
         *   &lt;simpleContent>
         *     &lt;extension base="&lt;>AttributeType">
         *       &lt;attribute name="Type" use="required" type="{http://www.w3.org/2001/XMLSchema}string" />
         *     &lt;/extension>
         *   &lt;/simpleContent>
         * &lt;/complexType>
         * </pre>
         * 
         * 
         */
        @XmlAccessorType(XmlAccessType.FIELD)
        @XmlType(name = "")
        public static class Attribute
            extends AttributeType
        {

            @XmlAttribute(name = "Type", required = true)
            protected String type;

            /**
             * Gets the value of the type property.
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getType() {
                return type;
            }

            /**
             * Sets the value of the type property.
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setType(String value) {
                this.type = value;
            }

        }

    }

}
