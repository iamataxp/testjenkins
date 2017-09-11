import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
public class TestJenkinsSuite {

    @Test
    public void testEchoName(){
        TestJenkins tt = new TestJenkins();
        String name = "Terry";
        assertEquals(name, tt.echoName(name));
    }


}
