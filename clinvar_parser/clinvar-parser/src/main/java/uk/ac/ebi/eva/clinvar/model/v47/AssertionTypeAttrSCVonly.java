//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.8-b130911.1802 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2017.08.17 at 04:29:30 PM BST 
//


package uk.ac.ebi.eva.clinvar.model.v47;

import javax.xml.bind.annotation.XmlEnum;
import javax.xml.bind.annotation.XmlEnumValue;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for AssertionTypeAttrSCVonly.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * <p>
 * <pre>
 * &lt;simpleType name="AssertionTypeAttrSCVonly">
 *   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}string">
 *     &lt;enumeration value="variation to included disease"/>
 *   &lt;/restriction>
 * &lt;/simpleType>
 * </pre>
 * 
 */
@XmlType(name = "AssertionTypeAttrSCVonly")
@XmlEnum
public enum AssertionTypeAttrSCVonly {

    @XmlEnumValue("variation to included disease")
    VARIATION_TO_INCLUDED_DISEASE("variation to included disease");
    private final String value;

    AssertionTypeAttrSCVonly(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static AssertionTypeAttrSCVonly fromValue(String v) {
        for (AssertionTypeAttrSCVonly c: AssertionTypeAttrSCVonly.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}
