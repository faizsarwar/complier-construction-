package compiler;

import java.util.Arrays;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.LinkedList;

public class SyntaxAnalyser
{
    static LinkedList<Token> _tokens;
    static final LinkedList<Token> _error;
    
    static {
        _error = new LinkedList<Token>();
    }
    
    public SyntaxAnalyser(final LinkedList<Token> tokens) {
        SyntaxAnalyser._tokens = tokens;
    }
    
    public void Start() {
        this.S();
        try {
            Throwable t = null;
            try {
                final FileWriter r = new FileWriter("GeneratedErrors.txt", true);
                try {
                    final BufferedWriter d = new BufferedWriter(r);
                    try {
                        final PrintWriter e = new PrintWriter(d);
                        try {
                            SyntaxAnalyser._error.forEach(element -> {
                                e.println("Classname: " + element.Class + " Value: " + element.Value);
                                System.out.println("< " + element.Class + " , " + element.Value + " , " + " >");
                                return;
                            });
                        }
                        finally {
                            if (e != null) {
                                e.close();
                            }
                        }
                        if (d != null) {
                            d.close();
                        }
                    }
                    finally {
                        if (t == null) {
                            final Throwable exception;
                            t = exception;
                        }
                        else {
                            final Throwable exception;
                            if (t != exception) {
                                t.addSuppressed(exception);
                            }
                        }
                        if (d != null) {
                            d.close();
                        }
                    }
                    if (r != null) {
                        r.close();
                    }
                }
                finally {
                    if (t == null) {
                        final Throwable exception2;
                        t = exception2;
                    }
                    else {
                        final Throwable exception2;
                        if (t != exception2) {
                            t.addSuppressed(exception2);
                        }
                    }
                    if (r != null) {
                        r.close();
                    }
                }
            }
            finally {
                if (t == null) {
                    final Throwable exception3;
                    t = exception3;
                }
                else {
                    final Throwable exception3;
                    if (t != exception3) {
                        t.addSuppressed(exception3);
                    }
                }
            }
        }
        catch (IOException i) {
            i.printStackTrace();
        }
    }
    
    private void S() {
        if (this.doesContain(Selectionset.first_DEFS)) {
            this.Defs();
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("$") || SyntaxAnalyser._tokens.get(0).Class.equals("$")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            SyntaxAnalyser._error.add(SyntaxAnalyser._tokens.get(0));
        }
    }
    
    private boolean Funcbody() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("{") || SyntaxAnalyser._tokens.get(0).Class.equals("{")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_FUNCMST) || this.doesContain(Selectionset.follow_FUNCMST)) {
                flag = this.Funcmst();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("}") || (SyntaxAnalyser._tokens.get(0).Class.equals("}") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Funcsst() {
        boolean flag;
        if (this.doesContain(Selectionset.first_SST)) {
            flag = this.Sst();
        }
        else if (this.doesContain(Selectionset.first_TRY)) {
            flag = this.Try();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Funcmst() {
        boolean flag;
        if (this.doesContain(Selectionset.first_FUNCSST)) {
            flag = this.Funcsst();
            if (this.doesContain(Selectionset.first_FUNCMST) || (this.doesContain(Selectionset.follow_FUNCMST) && flag)) {
                flag = this.Funcmst();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_FUNCMST)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("super") || SyntaxAnalyser._tokens.get(0).Class.equals("super")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_CLASSSST1)) {
                    flag = this.Classsst1();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_AM)) {
            flag = this.Am();
            if (this.doesContain(Selectionset.first_CLASSSST2) && flag) {
                flag = this.Classsst2();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("static") || SyntaxAnalyser._tokens.get(0).Class.equals("static")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_CLASSSST10)) {
                flag = this.Classsst10();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("protected") || SyntaxAnalyser._tokens.get(0).Class.equals("protected")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_STATICOPT) || this.doesContain(Selectionset.first_STATICOPT)) {
                flag = this.Staticopt();
                if (this.doesContain(Selectionset.first_CLASSSST4) && flag) {
                    flag = this.Classsst4();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst10() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_CLASSSST9)) {
                flag = this.Classsst9();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("final") || SyntaxAnalyser._tokens.get(0).Class.equals("final")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_DTOPT)) {
                flag = this.Dtopt();
                if (this.doesContain(Selectionset.first_SQBRACKOPT) || (this.doesContain(Selectionset.follow_SQBRACKOPT) && flag)) {
                    flag = this.Sqbrackopt();
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || (SyntaxAnalyser._tokens.get(0).Class.equals("id") && flag)) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_PARAM) || this.doesContain(Selectionset.follow_PARAM)) {
                                flag = this.Param();
                                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                    SyntaxAnalyser._tokens.remove(0);
                                    if (this.doesContain(Selectionset.first_FUNCBODY)) {
                                        flag = this.Funcbody();
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_CLASSSST6)) {
                flag = this.Classsst6();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_ROCONST)) {
            flag = this.Roconst();
            if (this.doesContain(Selectionset.first_CLASSSST7) && flag) {
                flag = this.Classsst7();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Dtopt() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst1() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_PARAM1) || this.doesContain(Selectionset.follow_PARAM1)) {
                flag = this.Param1();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Value.equals(";")) {
                        SyntaxAnalyser._tokens.remove(0);
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals(".") || SyntaxAnalyser._tokens.get(0).Class.equals(".")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_ID)) {
                flag = this.Id();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Am() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("public") || SyntaxAnalyser._tokens.get(0).Class.equals("public") || SyntaxAnalyser._tokens.get(0).Value.equals("private") || SyntaxAnalyser._tokens.get(0).Class.equals("private") || SyntaxAnalyser._tokens.get(0).Value.equals("protected") || SyntaxAnalyser._tokens.get(0).Class.equals("protected")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst2() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("final") || SyntaxAnalyser._tokens.get(0).Class.equals("final")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_SQBRACKOPT) || this.doesContain(Selectionset.follow_SQBRACKOPT)) {
                    flag = this.Sqbrackopt();
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || (SyntaxAnalyser._tokens.get(0).Class.equals("id") && flag)) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_PARAM) || this.doesContain(Selectionset.follow_PARAM)) {
                                flag = this.Param();
                                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                    SyntaxAnalyser._tokens.remove(0);
                                    if (this.doesContain(Selectionset.first_FUNCBODY)) {
                                        flag = this.Funcbody();
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_CLASSSST9)) {
                flag = this.Classsst9();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_ROCONST)) {
            flag = this.Roconst();
            if (this.doesContain(Selectionset.first_CLASSSST7) && flag) {
                flag = this.Classsst7();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("static") || SyntaxAnalyser._tokens.get(0).Class.equals("static")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_CLASSSST3)) {
                flag = this.Classsst3();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_CLASSSST6)) {
                flag = this.Classsst6();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst9() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_ARGLST) || this.doesContain(Selectionset.follow_ARGLST)) {
                flag = this.Arglst();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_INHERITOPT1) || this.doesContain(Selectionset.follow_INHERITOPT1)) {
                        flag = this.Inheritopt1();
                        if (this.doesContain(Selectionset.first_FUNCBODY) && flag) {
                            flag = this.Funcbody();
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("eq") || SyntaxAnalyser._tokens.get(0).Class.equals("eq")) {
                SyntaxAnalyser._tokens.remove(0);
                if (SyntaxAnalyser._tokens.get(0).Value.equals("new") || SyntaxAnalyser._tokens.get(0).Class.equals("new")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_PARAM1) || this.doesContain(Selectionset.follow_PARAM1)) {
                                flag = this.Param1();
                                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                    SyntaxAnalyser._tokens.remove(0);
                                    if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
                                        SyntaxAnalyser._tokens.remove(0);
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst7() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_INITOPT) || this.doesContain(Selectionset.follow_INITOPT)) {
                    flag = this.Initopt();
                    if (this.doesContain(Selectionset.first_DECLIST) && flag) {
                        flag = this.Declist();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_OBJST)) {
            flag = this.Objst();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst6() {
        boolean flag;
        if (this.doesContain(Selectionset.first_SQBRACK)) {
            flag = this.Sqbrack();
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || (SyntaxAnalyser._tokens.get(0).Class.equals("id") && flag)) {
                SyntaxAnalyser._tokens.remove(0);
                if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_PARAM) || this.doesContain(Selectionset.follow_PARAM)) {
                        flag = this.Param();
                        if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_FUNCBODY)) {
                                flag = this.Funcbody();
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_CLASSSST8)) {
                flag = this.Classsst8();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst8() {
        boolean flag;
        if (this.doesContain(Selectionset.first_INITOPT) || this.doesContain(Selectionset.first_INITOPT)) {
            flag = this.Initopt();
            if (this.doesContain(Selectionset.first_DECLIST) && flag) {
                flag = this.Declist();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_PARAM) || this.doesContain(Selectionset.follow_PARAM)) {
                flag = this.Param();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_FUNCBODY)) {
                        flag = this.Funcbody();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst3() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("final") || SyntaxAnalyser._tokens.get(0).Class.equals("final")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_SQBRACKOPT) || this.doesContain(Selectionset.follow_SQBRACKOPT)) {
                    flag = this.Sqbrackopt();
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || (SyntaxAnalyser._tokens.get(0).Class.equals("id") && flag)) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_PARAM) || this.doesContain(Selectionset.follow_PARAM)) {
                                flag = this.Param();
                                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                    SyntaxAnalyser._tokens.remove(0);
                                    if (this.doesContain(Selectionset.first_FUNCBODY)) {
                                        flag = this.Funcbody();
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_CLASSSST6)) {
                flag = this.Classsst6();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_ROCONST)) {
            flag = this.Roconst();
            if (this.doesContain(Selectionset.first_CLASSSST7) && flag) {
                flag = this.Classsst7();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_OBJST)) {
            flag = this.Objst();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst4() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("final") || SyntaxAnalyser._tokens.get(0).Class.equals("final")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_SQBRACKOPT) || this.doesContain(Selectionset.follow_SQBRACKOPT)) {
                    flag = this.Sqbrackopt();
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || (SyntaxAnalyser._tokens.get(0).Class.equals("id") && flag)) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_PARAM) || this.doesContain(Selectionset.follow_PARAM)) {
                                flag = this.Param();
                                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                    SyntaxAnalyser._tokens.remove(0);
                                    if (this.doesContain(Selectionset.first_FUNCBODY)) {
                                        flag = this.Funcbody();
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_CLASSSST6)) {
                flag = this.Classsst6();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_ROCONST)) {
            flag = this.Roconst();
            if (this.doesContain(Selectionset.first_CLASSSST5) && flag) {
                flag = this.Classsst5();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_OBJST)) {
            flag = this.Objst();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsst5() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_INITOPT) || this.doesContain(Selectionset.follow_INITOPT)) {
                    flag = this.Initopt();
                    if (this.doesContain(Selectionset.first_DECLIST) && flag) {
                        flag = this.Declist();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_OBJST)) {
            flag = this.Objst();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sqbrack() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("[") || SyntaxAnalyser._tokens.get(0).Class.equals("[")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_SQBRACKC)) {
                flag = this.Sqbrackc();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Roconst() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("readonly") || SyntaxAnalyser._tokens.get(0).Class.equals("readonly")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("const") || SyntaxAnalyser._tokens.get(0).Class.equals("const")) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classbody() {
        boolean flag;
        if (this.doesContain(Selectionset.first_CLASS_SST)) {
            flag = this.Classsst();
            if (this.doesContain(Selectionset.first_CLASSBODY) || (this.doesContain(Selectionset.follow_CLASSBODY) && flag)) {
                flag = this.Classbody();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_CLASSBODY)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Loopsst() {
        boolean flag = true;
        if (this.doesContain(Selectionset.first_SST)) {
            flag = this.Sst();
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("break") || SyntaxAnalyser._tokens.get(0).Class.equals("break")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("continue") || SyntaxAnalyser._tokens.get(0).Class.equals("continue")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_TRY)) {
            flag = this.Try();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Loopmst() {
        boolean flag;
        if (this.doesContain(Selectionset.first_LOOPSST)) {
            flag = this.Loopsst();
            if (this.doesContain(Selectionset.first_LOOPMST) || (this.doesContain(Selectionset.follow_LOOPMST) && flag)) {
                flag = this.Loopmst();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_LOOPMST)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Loopbody() {
        boolean flag;
        if (this.doesContain(Selectionset.first_LOOPSST)) {
            flag = this.Loopsst();
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("{") || SyntaxAnalyser._tokens.get(0).Class.equals("{")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_LOOPMST) || this.doesContain(Selectionset.follow_LOOPMST)) {
                flag = this.Loopmst();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("}") || (SyntaxAnalyser._tokens.get(0).Class.equals("}") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Whilest() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("while") || SyntaxAnalyser._tokens.get(0).Class.equals("while")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_OE)) {
                    flag = this.Oe();
                    if (this.doesContain(Selectionset.first_ASSIGNOPT) || (this.doesContain(Selectionset.follow_ASSIGNOPT) && flag)) {
                        flag = this.Assignopt();
                        if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_LOOPBODY)) {
                                flag = this.Loopbody();
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Assignopt() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_C4)) {
                flag = this.C4();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_ASSIGNOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Dowhile() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("do") || SyntaxAnalyser._tokens.get(0).Class.equals("do")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_LOOPBODY)) {
                flag = this.Loopbody();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("while") || (SyntaxAnalyser._tokens.get(0).Class.equals("while") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (this.doesContain(Selectionset.first_OE)) {
                            flag = this.Oe();
                            if (this.doesContain(Selectionset.first_ASSIGNOPT) || (this.doesContain(Selectionset.follow_ASSIGNOPT) && flag)) {
                                flag = this.Assignopt();
                                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                    SyntaxAnalyser._tokens.remove(0);
                                    if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
                                        SyntaxAnalyser._tokens.remove(0);
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Forst() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("for") || SyntaxAnalyser._tokens.get(0).Class.equals("for")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_C1)) {
                    flag = this.C1();
                    if (this.doesContain(Selectionset.first_C2) || (this.doesContain(Selectionset.follow_C2) && flag)) {
                        flag = this.C2();
                        if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_C3) || this.doesContain(Selectionset.follow_C3)) {
                                flag = this.C3();
                                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                    SyntaxAnalyser._tokens.remove(0);
                                    if (this.doesContain(Selectionset.first_LOOPBODY)) {
                                        flag = this.Loopbody();
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean C1() {
        boolean flag = true;
        if (this.doesContain(Selectionset.first_DECFB)) {
            flag = this.Decfb();
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else if (this.doesContain(Selectionset.first_ASSST)) {
            flag = this.Assst();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean C2() {
        boolean flag;
        if (this.doesContain(Selectionset.first_OEOPT) || this.doesContain(Selectionset.follow_OEOPT)) {
            flag = this.Oeopt();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Incordec() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("++") || SyntaxAnalyser._tokens.get(0).Class.equals("++") || SyntaxAnalyser._tokens.get(0).Value.equals("--") || SyntaxAnalyser._tokens.get(0).Class.equals("--")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Assign2() {
        boolean flag;
        if (this.doesContain(Selectionset.first_ASSIGN)) {
            flag = this.Assign2();
        }
        else {
            if (this.doesContain(Selectionset.follow_ASSIGN2)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Assign1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_OE)) {
            flag = this.Oe();
            if (this.doesContain(Selectionset.first_ASSIGN2) || (this.doesContain(Selectionset.follow_ASSIGN2) && flag)) {
                flag = this.Assign2();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Assign() {
        boolean flag;
        if (this.doesContain(Selectionset.first_AOP)) {
            flag = this.Aop();
            if (this.doesContain(Selectionset.first_ASSIGN1) && flag) {
                flag = this.Assign1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Assignst() {
        boolean flag;
        if (this.doesContain(Selectionset.first_IDS)) {
            flag = this.Ids();
            if (this.doesContain(Selectionset.first_ASSIGN) && flag) {
                flag = this.Assign();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Assst() {
        boolean flag;
        if (this.doesContain(Selectionset.first_ASSIGNST)) {
            flag = this.Assignst();
            if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean C5() {
        boolean flag;
        if (this.doesContain(Selectionset.first_ASSIGN)) {
            flag = this.Assign();
        }
        else if (this.doesContain(Selectionset.first_INCORDEC)) {
            flag = this.Incordec();
        }
        else {
            if (this.doesContain(Selectionset.follow_C5)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean C4() {
        boolean flag;
        if (this.doesContain(Selectionset.first_IDS)) {
            flag = this.Ids();
            if (this.doesContain(Selectionset.first_C5) || (this.doesContain(Selectionset.follow_C5) && flag)) {
                flag = this.C5();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_INCORDEC)) {
            flag = this.Incordec();
            if (this.doesContain(Selectionset.first_IDS) && flag) {
                flag = this.Ids();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean C3() {
        boolean flag;
        if (this.doesContain(Selectionset.first_C4)) {
            flag = this.C4();
        }
        else {
            if (this.doesContain(Selectionset.follow_C3)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Ifelse() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("if") || SyntaxAnalyser._tokens.get(0).Class.equals("if")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_OE)) {
                    flag = this.Oe();
                    if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || SyntaxAnalyser._tokens.get(0).Class.equals(")")) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (this.doesContain(Selectionset.first_FUNCBODY) && flag) {
                            flag = this.Funcbody();
                            if (this.doesContain(Selectionset.first_ELSE) || (this.doesContain(Selectionset.follow_ELSE) && flag)) {
                                flag = this.Else();
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Else() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("else") || SyntaxAnalyser._tokens.get(0).Class.equals("else")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_OEOPT) || this.doesContain(Selectionset.follow_OEOPT)) {
                    flag = this.Oeopt();
                    if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (this.doesContain(Selectionset.first_FUNCBODY)) {
                            flag = this.Funcbody();
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_ELSE)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Param() {
        boolean flag;
        if (this.doesContain(Selectionset.first_DTOPT)) {
            flag = this.Dtopt();
            if (this.doesContain(Selectionset.first_SQBRACKOPT) || (this.doesContain(Selectionset.follow_SQBRACKOPT) && flag)) {
                flag = this.Sqbrackopt();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || (SyntaxAnalyser._tokens.get(0).Class.equals("id") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_PARAMINIT) || this.doesContain(Selectionset.follow_PARAMINIT)) {
                        flag = this.Paraminit();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_PARAM)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Paraminit() {
        boolean flag;
        if (this.doesContain(Selectionset.first_PARAMLST) || this.doesContain(Selectionset.follow_PARAMLST)) {
            flag = this.Paramlst();
        }
        else if (this.doesContain(Selectionset.first_INIT)) {
            flag = this.Init();
            if (this.doesContain(Selectionset.first_PARAMLST2) && flag) {
                flag = this.Paramlst2();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Paramlst() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
                SyntaxAnalyser._tokens.remove(0);
                if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_PARAMINIT) || this.doesContain(Selectionset.follow_PARAMINIT)) {
                        flag = this.Paraminit();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_PARAMLST)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Paramlst2() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
                SyntaxAnalyser._tokens.remove(0);
                if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_INIT)) {
                        flag = this.Init();
                        if (this.doesContain(Selectionset.first_PARAMLST3) || (this.doesContain(Selectionset.follow_PARAMLST3) && flag)) {
                            flag = this.Paramlst3();
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Paramlst3() {
        boolean flag;
        if (this.doesContain(Selectionset.first_PARAMLST2)) {
            flag = this.Paramlst2();
        }
        else {
            if (this.doesContain(Selectionset.follow_PARAMLST3)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sqbrackopt() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("[") || SyntaxAnalyser._tokens.get(0).Class.equals("[")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_SQBRACKC)) {
                flag = this.Sqbrackc();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_SQBRACKOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sqbrackc() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("]") || SyntaxAnalyser._tokens.get(0).Class.equals("]")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("]") || SyntaxAnalyser._tokens.get(0).Class.equals("]")) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Param1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_PARAM2)) {
            flag = this.Param2();
        }
        else {
            if (this.doesContain(Selectionset.follow_PARAM1)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Param2() {
        boolean flag;
        if (this.doesContain(Selectionset.first_OE)) {
            flag = this.Oe();
            if (this.doesContain(Selectionset.first_PARAM3) || (this.doesContain(Selectionset.follow_PARAM3) && flag)) {
                flag = this.Param3();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Param3() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_PARAM2)) {
                flag = this.Param2();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_PARAM3)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classsig() {
        boolean flag;
        if (this.doesContain(Selectionset.first_AMOPT) || this.doesContain(Selectionset.follow_AMOPT)) {
            flag = this.Amopt();
            if (this.doesContain(Selectionset.first_STATICOPT) || (this.doesContain(Selectionset.follow_STATICOPT) && flag)) {
                flag = this.Staticopt();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("class") || SyntaxAnalyser._tokens.get(0).Class.equals("class")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (SyntaxAnalyser._tokens.get(0).Class.equals("id") || SyntaxAnalyser._tokens.get(0).Value.equals("id")) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (this.doesContain(Selectionset.first_INHERITOPT) || (this.doesContain(Selectionset.follow_INHERITOPT) && flag)) {
                            flag = this.Inheritopt();
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Classst() {
        boolean flag;
        if (this.doesContain(Selectionset.first_CLASSSIG)) {
            flag = this.Classsig();
            if (SyntaxAnalyser._tokens.get(0).Value.equals("{") || SyntaxAnalyser._tokens.get(0).Class.equals("{")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_CLASSBODY) || (this.doesContain(Selectionset.follow_CLASSBODY) && flag)) {
                    flag = this.Classbody();
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("}") || (SyntaxAnalyser._tokens.get(0).Class.equals("}") && flag)) {
                        SyntaxAnalyser._tokens.remove(0);
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Inheritopt() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("inherit") || SyntaxAnalyser._tokens.get(0).Class.equals("inherit")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_INHERITOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Inheritopt1() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("inherit") || SyntaxAnalyser._tokens.get(0).Class.equals("inherit")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_SUPERTHIS)) {
                flag = this.Superthis();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || (SyntaxAnalyser._tokens.get(0).Class.equals("(") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_ARGLST) || this.doesContain(Selectionset.follow_ARGLST)) {
                        flag = this.Arglst();
                        if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                            SyntaxAnalyser._tokens.remove(0);
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_INHERITOPT1)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Superthis() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("super") || SyntaxAnalyser._tokens.get(0).Class.equals("super")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("this") || SyntaxAnalyser._tokens.get(0).Class.equals("this")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Arglst() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_ARGLIST1) || this.doesContain(Selectionset.follow_ARGLIST1)) {
                    flag = this.Arglist1();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_ARGLST)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Arglist1() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
                SyntaxAnalyser._tokens.remove(0);
                if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_ARGLIST1) || this.doesContain(Selectionset.follow_ARGLIST1)) {
                        flag = this.Arglist1();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_ARGLIST1)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Objst() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_SQBRACKOPT) || this.doesContain(Selectionset.follow_SQBRACKOPT)) {
                flag = this.Sqbrackopt();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || (SyntaxAnalyser._tokens.get(0).Class.equals("id") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("=") || SyntaxAnalyser._tokens.get(0).Class.equals("=")) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                                SyntaxAnalyser._tokens.remove(0);
                                if (this.doesContain(Selectionset.first_PARAM1) || this.doesContain(Selectionset.follow_PARAM1)) {
                                    flag = this.Param1();
                                    if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                        SyntaxAnalyser._tokens.remove(0);
                                        if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
                                            SyntaxAnalyser._tokens.remove(0);
                                        }
                                        else {
                                            flag = this.AddError();
                                        }
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Oe() {
        boolean flag;
        if (this.doesContain(Selectionset.first_AE)) {
            flag = this.Ae();
            if (this.doesContain(Selectionset.first_OE1) || (this.doesContain(Selectionset.follow_OE1) && flag)) {
                flag = this.Oe1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Oe1() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("|") || SyntaxAnalyser._tokens.get(0).Class.equals("|")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_AE)) {
                flag = this.Ae();
                if (this.doesContain(Selectionset.first_OE1) || (this.doesContain(Selectionset.follow_OE1) && flag)) {
                    flag = this.Oe1();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_OE1)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Ae() {
        boolean flag;
        if (this.doesContain(Selectionset.first_RE)) {
            flag = this.Re();
            if (this.doesContain(Selectionset.first_AE1) || (this.doesContain(Selectionset.follow_AE1) && flag)) {
                flag = this.Ae1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Ae1() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("&") || SyntaxAnalyser._tokens.get(0).Class.equals("&")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_RE)) {
                flag = this.Re();
                if (this.doesContain(Selectionset.first_AE1) || (this.doesContain(Selectionset.follow_AE1) && flag)) {
                    flag = this.Ae1();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_AE1)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Re() {
        boolean flag;
        if (this.doesContain(Selectionset.first_E)) {
            flag = this.E();
            if (this.doesContain(Selectionset.first_RE1) || (this.doesContain(Selectionset.follow_RE1) && flag)) {
                flag = this.Re1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Re1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_ROP)) {
            flag = this.Rop();
            if (this.doesContain(Selectionset.first_E) && flag) {
                flag = this.E();
                if (this.doesContain(Selectionset.first_RE1) || (this.doesContain(Selectionset.follow_RE1) && flag)) {
                    flag = this.Re1();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_RE1)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean E() {
        boolean flag;
        if (this.doesContain(Selectionset.first_T)) {
            flag = this.T();
            if (this.doesContain(Selectionset.first_E1) || (this.doesContain(Selectionset.follow_E1) && flag)) {
                flag = this.E1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean E1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_PM)) {
            flag = this.Pm();
            if (this.doesContain(Selectionset.first_T) && flag) {
                flag = this.T();
                if (this.doesContain(Selectionset.first_E1) || (this.doesContain(Selectionset.follow_E1) && flag)) {
                    flag = this.E1();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_E1)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean T() {
        boolean flag;
        if (this.doesContain(Selectionset.first_F)) {
            flag = this.F();
            if (this.doesContain(Selectionset.first_T1) || (this.doesContain(Selectionset.follow_T1) && flag)) {
                flag = this.T1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean T1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_MDM)) {
            flag = this.Mdm();
            if (this.doesContain(Selectionset.first_F) && flag) {
                flag = this.F();
                if (this.doesContain(Selectionset.first_T1) || (this.doesContain(Selectionset.follow_T1) && flag)) {
                    flag = this.T1();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_T1)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean F() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("literal") || SyntaxAnalyser._tokens.get(0).Class.equals("literal")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("!") || SyntaxAnalyser._tokens.get(0).Class.equals("!")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_F)) {
                flag = this.F();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_OE)) {
                flag = this.Oe();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || SyntaxAnalyser._tokens.get(0).Class.equals(")")) {
                    SyntaxAnalyser._tokens.remove(0);
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_INCORDEC)) {
            flag = this.Incordec();
            if (this.doesContain(Selectionset.first_IDS) && flag) {
                flag = this.Ids();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_IDS)) {
            flag = this.Ids();
            if (this.doesContain(Selectionset.first_F1) || (this.doesContain(Selectionset.follow_F1) && flag)) {
                flag = this.F1();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean F1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_INCORDECOPT) || this.doesContain(Selectionset.follow_INCORDECOPT)) {
            flag = this.Incordecopt();
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_PARAM1) || this.doesContain(Selectionset.follow_PARAM1)) {
                flag = this.Param1();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                if (this.doesContain(Selectionset.follow_F1)) {
                    return true;
                }
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Incordecopt() {
        boolean flag;
        if (this.doesContain(Selectionset.first_INCORDEC)) {
            flag = this.Incordec();
        }
        else {
            if (this.doesContain(Selectionset.follow_INCORDECOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Try() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("try") || SyntaxAnalyser._tokens.get(0).Class.equals("try")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_FUNCBODY)) {
                flag = this.Funcbody();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("catch") || (SyntaxAnalyser._tokens.get(0).Class.equals("catch") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (SyntaxAnalyser._tokens.get(0).Value.equals("exception") || SyntaxAnalyser._tokens.get(0).Class.equals("exception")) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_IDOPT) || this.doesContain(Selectionset.follow_IDOPT)) {
                                flag = this.Idopt();
                                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                    SyntaxAnalyser._tokens.remove(0);
                                    if (this.doesContain(Selectionset.first_FUNCBODY)) {
                                        flag = this.Funcbody();
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Idopt() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            if (this.doesContain(Selectionset.follow_IDOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Ids() {
        boolean flag;
        if (this.doesContain(Selectionset.first_ID)) {
            flag = this.Id();
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("this") || SyntaxAnalyser._tokens.get(0).Class.equals("this")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals(".") || SyntaxAnalyser._tokens.get(0).Class.equals(".")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_ID)) {
                    flag = this.Id();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Id() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_ID1) || this.doesContain(Selectionset.follow_ID1)) {
                flag = this.Id1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Id1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_IDM) || this.doesContain(Selectionset.follow_IDM)) {
            flag = this.Idm();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Idm() {
        boolean flag;
        if (this.doesContain(Selectionset.first_DOT) || this.doesContain(Selectionset.follow_DOT)) {
            flag = this.Dot();
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("[") || SyntaxAnalyser._tokens.get(0).Class.equals("[")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_OE)) {
                flag = this.Oe();
                if (this.doesContain(Selectionset.first_ID2) && flag) {
                    flag = this.Id2();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Id2() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("]") || SyntaxAnalyser._tokens.get(0).Class.equals("]")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_DOT) || this.doesContain(Selectionset.follow_DOT)) {
                flag = this.Dot();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_OE)) {
                flag = this.Oe();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("]") || (SyntaxAnalyser._tokens.get(0).Class.equals("]") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_DOT) || this.doesContain(Selectionset.follow_DOT)) {
                        flag = this.Dot();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Dot() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(".") || SyntaxAnalyser._tokens.get(0).Class.equals(".")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_ID)) {
                flag = this.Id();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_DOT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Rop() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(">") || SyntaxAnalyser._tokens.get(0).Class.equals(">") || SyntaxAnalyser._tokens.get(0).Value.equals("<") || SyntaxAnalyser._tokens.get(0).Class.equals("<") || SyntaxAnalyser._tokens.get(0).Value.equals("<=") || SyntaxAnalyser._tokens.get(0).Class.equals("<=") || SyntaxAnalyser._tokens.get(0).Value.equals(">=") || SyntaxAnalyser._tokens.get(0).Class.equals(">=") || SyntaxAnalyser._tokens.get(0).Value.equals("!=") || SyntaxAnalyser._tokens.get(0).Class.equals("!=") || SyntaxAnalyser._tokens.get(0).Value.equals("==") || SyntaxAnalyser._tokens.get(0).Class.equals("==")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Aop() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("=") || SyntaxAnalyser._tokens.get(0).Class.equals("=") || SyntaxAnalyser._tokens.get(0).Value.equals("-=") || SyntaxAnalyser._tokens.get(0).Class.equals("-=") || SyntaxAnalyser._tokens.get(0).Value.equals("+=") || SyntaxAnalyser._tokens.get(0).Class.equals("+=") || SyntaxAnalyser._tokens.get(0).Value.equals("*=") || SyntaxAnalyser._tokens.get(0).Class.equals("*=") || SyntaxAnalyser._tokens.get(0).Value.equals("/=") || SyntaxAnalyser._tokens.get(0).Class.equals("/=") || SyntaxAnalyser._tokens.get(0).Value.equals("%=") || SyntaxAnalyser._tokens.get(0).Class.equals("%=")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Pm() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("+") || SyntaxAnalyser._tokens.get(0).Class.equals("+") || SyntaxAnalyser._tokens.get(0).Value.equals("-") || SyntaxAnalyser._tokens.get(0).Class.equals("-")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Mdm() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("*") || SyntaxAnalyser._tokens.get(0).Class.equals("*") || SyntaxAnalyser._tokens.get(0).Value.equals("/") || SyntaxAnalyser._tokens.get(0).Class.equals("/") || SyntaxAnalyser._tokens.get(0).Value.equals("%") || SyntaxAnalyser._tokens.get(0).Class.equals("%")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Twodarrinitopt1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_TWODARRINIT)) {
            flag = this.Twodarrinit();
        }
        else if (this.doesContain(Selectionset.first_ID)) {
            flag = this.Ids();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Twodarrinit() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("{") || SyntaxAnalyser._tokens.get(0).Class.equals("{")) {
            SyntaxAnalyser._tokens.remove(0);
            flag = (this.doesContain(Selectionset.first_TWODARRINIT1) ? this.Twodarrinit1() : this.AddError());
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Twodarrinit1() {
        boolean flag = true;
        if (this.doesContain(Selectionset.first_ARRINIT)) {
            flag = this.Arrinit();
            if (this.doesContain(Selectionset.first_ARR) || (this.doesContain(Selectionset.follow_ARR) && flag)) {
                flag = this.Arr();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("}") || (SyntaxAnalyser._tokens.get(0).Class.equals("}") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("}") || SyntaxAnalyser._tokens.get(0).Class.equals("}")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Arr() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_ARRINIT)) {
                flag = this.Arrinit();
                if (this.doesContain(Selectionset.first_ARR) || (this.doesContain(Selectionset.follow_ARR) && flag)) {
                    flag = this.Arr();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_ARR)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sst() {
        boolean flag = true;
        if (this.doesContain(Selectionset.first_WHILEST)) {
            flag = this.Whilest();
        }
        else if (this.doesContain(Selectionset.first_FORST)) {
            flag = this.Forst();
        }
        else if (this.doesContain(Selectionset.first_IFELSE)) {
            flag = this.Ifelse();
        }
        else if (this.doesContain(Selectionset.first_DOWHILEST)) {
            flag = this.Dowhile();
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("return") || SyntaxAnalyser._tokens.get(0).Class.equals("return")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_OEOPT) || this.doesContain(Selectionset.follow_OEOPT)) {
                flag = this.Oeopt();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_INCORDEC)) {
            flag = this.Incordec();
            if (this.doesContain(Selectionset.first_IDS) && flag) {
                flag = this.Ids();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_SST5)) {
                flag = this.Sst5();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("const") || SyntaxAnalyser._tokens.get(0).Class.equals("const")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || SyntaxAnalyser._tokens.get(0).Class.equals("dt")) {
                SyntaxAnalyser._tokens.remove(0);
                if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_INITOPT) || this.doesContain(Selectionset.follow_INITOPT)) {
                        flag = this.Initopt();
                        if (this.doesContain(Selectionset.first_DECLIST) && flag) {
                            flag = this.Declist();
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_SST2)) {
                flag = this.Sst2();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("this") || SyntaxAnalyser._tokens.get(0).Class.equals("this")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals(".") || SyntaxAnalyser._tokens.get(0).Class.equals(".")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_ID)) {
                    flag = this.Id();
                    if (this.doesContain(Selectionset.first_SST1) && flag) {
                        flag = this.Sst1();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sst1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_INCORDEC)) {
            flag = this.Incordec();
            if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_ASSIGN)) {
            flag = this.Assign();
            if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_PARAM1) || this.doesContain(Selectionset.follow_PARAM1)) {
                flag = this.Param1();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                }
                else {
                    flag = this.AddError();
                }
                if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
                    SyntaxAnalyser._tokens.remove(0);
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sst2() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(".") || SyntaxAnalyser._tokens.get(0).Class.equals(".")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_ID)) {
                flag = this.Id();
                if (this.doesContain(Selectionset.first_SST1) && flag) {
                    flag = this.Sst1();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_INCORDEC)) {
            flag = this.Incordec();
            if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_ASSIGN)) {
            flag = this.Assign();
            if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_PARAM1) || this.doesContain(Selectionset.follow_PARAM1)) {
                flag = this.Param1();
                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_SST4)) {
                        flag = this.Sst4();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("[") || SyntaxAnalyser._tokens.get(0).Class.equals("[")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_SST3)) {
                flag = this.Sst3();
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("=") || SyntaxAnalyser._tokens.get(0).Class.equals("=")) {
                SyntaxAnalyser._tokens.remove(0);
                if (SyntaxAnalyser._tokens.get(0).Value.equals("new") || SyntaxAnalyser._tokens.get(0).Class.equals("new")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (this.doesContain(Selectionset.first_PARAM1) || this.doesContain(Selectionset.follow_PARAM1)) {
                                flag = this.Param1();
                                if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                    SyntaxAnalyser._tokens.remove(0);
                                    if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
                                        SyntaxAnalyser._tokens.remove(0);
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sst4() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals(".") || SyntaxAnalyser._tokens.get(0).Class.equals(".")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_ID1) || this.doesContain(Selectionset.follow_ID1)) {
                    flag = this.Id1();
                    if (this.doesContain(Selectionset.first_SST1) && flag) {
                        flag = this.Sst1();
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sst3() {
        boolean flag;
        if (this.doesContain(Selectionset.first_OE)) {
            flag = this.Oe();
            if (this.doesContain(Selectionset.first_ID2) && flag) {
                flag = this.Id2();
                if (this.doesContain(Selectionset.first_SST1) && flag) {
                    flag = this.Sst1();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (this.doesContain(Selectionset.first_SQBRACKC)) {
            flag = this.Sqbrackc();
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || (SyntaxAnalyser._tokens.get(0).Class.equals("id") && flag)) {
                SyntaxAnalyser._tokens.remove(0);
                if (SyntaxAnalyser._tokens.get(0).Value.equals("=") || SyntaxAnalyser._tokens.get(0).Class.equals("=")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("new") || SyntaxAnalyser._tokens.get(0).Class.equals("new")) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                            SyntaxAnalyser._tokens.remove(0);
                            if (SyntaxAnalyser._tokens.get(0).Value.equals("(") || SyntaxAnalyser._tokens.get(0).Class.equals("(")) {
                                SyntaxAnalyser._tokens.remove(0);
                                if (this.doesContain(Selectionset.first_PARAM1) || this.doesContain(Selectionset.follow_PARAM1)) {
                                    flag = this.Param1();
                                    if (SyntaxAnalyser._tokens.get(0).Value.equals(")") || (SyntaxAnalyser._tokens.get(0).Class.equals(")") && flag)) {
                                        SyntaxAnalyser._tokens.remove(0);
                                        if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
                                            SyntaxAnalyser._tokens.remove(0);
                                        }
                                        else {
                                            flag = this.AddError();
                                        }
                                    }
                                    else {
                                        flag = this.AddError();
                                    }
                                }
                                else {
                                    flag = this.AddError();
                                }
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sst5() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("[") || SyntaxAnalyser._tokens.get(0).Class.equals("[")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_OEOPT) || this.doesContain(Selectionset.follow_OEOPT)) {
                flag = this.Oeopt();
                if (this.doesContain(Selectionset.first_SST6) && flag) {
                    flag = this.Sst6();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_INITOPT) || this.doesContain(Selectionset.follow_INITOPT)) {
                flag = this.Initopt();
                if (this.doesContain(Selectionset.first_DECLIST) && flag) {
                    flag = this.Declist();
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Sst6() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("]") || SyntaxAnalyser._tokens.get(0).Class.equals("]")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_ARRINITOPT) || this.doesContain(Selectionset.follow_ARRINITOPT)) {
                    flag = this.Arrinitopt();
                    if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                        SyntaxAnalyser._tokens.remove(0);
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_OEOPT) || this.doesContain(Selectionset.follow_OEOPT)) {
                flag = this.Oeopt();
                if (SyntaxAnalyser._tokens.get(0).Value.equals("]") || (SyntaxAnalyser._tokens.get(0).Class.equals("]") && flag)) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                        SyntaxAnalyser._tokens.remove(0);
                        if (this.doesContain(Selectionset.first_TWODARRINITOPT) || this.doesContain(Selectionset.follow_TWODARRINITOPT)) {
                            flag = this.Twodarrinitopt();
                            if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || (SyntaxAnalyser._tokens.get(0).Class.equals(";") && flag)) {
                                SyntaxAnalyser._tokens.remove(0);
                            }
                            else {
                                flag = this.AddError();
                            }
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Defs() {
        boolean flag;
        if (this.doesContain(Selectionset.first_CLASS_SST)) {
            flag = this.Classst();
            if (this.doesContain(Selectionset.first_DEFS) && flag) {
                flag = this.Defs();
            }
            else {
                if (SyntaxAnalyser._tokens.get(0).Value.equals("$") || SyntaxAnalyser._tokens.get(0).Class.equals("$")) {
                    return false;
                }
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Amopt() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("public") || SyntaxAnalyser._tokens.get(0).Class.equals("public") || SyntaxAnalyser._tokens.get(0).Value.equals("private") || SyntaxAnalyser._tokens.get(0).Class.equals("private") || SyntaxAnalyser._tokens.get(0).Value.equals("protected") || SyntaxAnalyser._tokens.get(0).Class.equals("protected")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            if (this.doesContain(Selectionset.follow_AMOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Staticopt() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("static") || SyntaxAnalyser._tokens.get(0).Class.equals("static")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            if (this.doesContain(Selectionset.follow_STATICOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Init() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("=") || SyntaxAnalyser._tokens.get(0).Class.equals("=")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_INIT1)) {
                flag = this.Init1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Init1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_OE)) {
            flag = this.Oe();
            if (this.doesContain(Selectionset.first_INIT2) || (this.doesContain(Selectionset.follow_INIT2) && flag)) {
                flag = this.Init2();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Init2() {
        boolean flag;
        if (this.doesContain(Selectionset.first_INIT)) {
            flag = this.Init();
        }
        else {
            if (this.doesContain(Selectionset.follow_INIT2)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Initopt() {
        boolean flag;
        if (this.doesContain(Selectionset.first_INIT)) {
            flag = this.Init();
        }
        else {
            if (this.doesContain(Selectionset.follow_INITOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Declist() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(";") || SyntaxAnalyser._tokens.get(0).Class.equals(";")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                SyntaxAnalyser._tokens.remove(0);
                if (this.doesContain(Selectionset.first_INITOPT) || this.doesContain(Selectionset.follow_INITOPT)) {
                    flag = this.Initopt();
                    if (this.doesContain(Selectionset.first_DECLIST) && flag) {
                        flag = this.Declist();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Decfb() {
        boolean flag;
        if (this.doesContain(Selectionset.first_CONSTOPT) || this.doesContain(Selectionset.follow_CONSTOPT)) {
            flag = this.Constopt();
            if (SyntaxAnalyser._tokens.get(0).Value.equals("dt") || (SyntaxAnalyser._tokens.get(0).Class.equals("dt") && flag)) {
                SyntaxAnalyser._tokens.remove(0);
                if (SyntaxAnalyser._tokens.get(0).Value.equals("id") || SyntaxAnalyser._tokens.get(0).Class.equals("id")) {
                    SyntaxAnalyser._tokens.remove(0);
                    if (this.doesContain(Selectionset.first_INITOPT) || this.doesContain(Selectionset.follow_INITOPT)) {
                        flag = this.Initopt();
                        if (this.doesContain(Selectionset.first_DECLIST) && flag) {
                            flag = this.Declist();
                        }
                        else {
                            flag = this.AddError();
                        }
                    }
                    else {
                        flag = this.AddError();
                    }
                }
                else {
                    flag = this.AddError();
                }
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Constopt() {
        boolean flag = true;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("const") || SyntaxAnalyser._tokens.get(0).Class.equals("const")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            if (this.doesContain(Selectionset.follow_CONSTOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Arrinitopt() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("=") || SyntaxAnalyser._tokens.get(0).Class.equals("=")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_ARRINITOPT1)) {
                flag = this.Arrinitopt1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_ARRINITOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Arrinitopt1() {
        boolean flag;
        if (this.doesContain(Selectionset.first_ARRINIT)) {
            flag = this.Arrinit();
        }
        else if (this.doesContain(Selectionset.first_IDS)) {
            flag = this.Ids();
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Arrinit() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("{") || SyntaxAnalyser._tokens.get(0).Class.equals("{")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_ARRINIT1)) {
                flag = this.Arrinit1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Arrinit1() {
        boolean flag = true;
        if (this.doesContain(Selectionset.first_VAL)) {
            flag = this.Val();
            if (SyntaxAnalyser._tokens.get(0).Value.equals("}") || (SyntaxAnalyser._tokens.get(0).Class.equals("}") && flag)) {
                SyntaxAnalyser._tokens.remove(0);
            }
            else {
                flag = this.AddError();
            }
        }
        else if (SyntaxAnalyser._tokens.get(0).Value.equals("}") || SyntaxAnalyser._tokens.get(0).Class.equals("}")) {
            SyntaxAnalyser._tokens.remove(0);
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Val() {
        boolean flag;
        if (this.doesContain(Selectionset.first_OE)) {
            flag = this.Oe();
            if (this.doesContain(Selectionset.first_VAL2) || (this.doesContain(Selectionset.follow_VAL2) && flag)) {
                flag = this.Val2();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Val2() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals(",") || SyntaxAnalyser._tokens.get(0).Class.equals(",")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_VAL)) {
                flag = this.Val();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_VAL2)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Oeopt() {
        boolean flag;
        if (this.doesContain(Selectionset.first_OE)) {
            flag = this.Oe();
        }
        else {
            if (this.doesContain(Selectionset.follow_OEOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean Twodarrinitopt() {
        boolean flag;
        if (SyntaxAnalyser._tokens.get(0).Value.equals("=") || SyntaxAnalyser._tokens.get(0).Class.equals("=")) {
            SyntaxAnalyser._tokens.remove(0);
            if (this.doesContain(Selectionset.first_TWODARRINITOPT1) || this.doesContain(Selectionset.follow_TWODARRINITOPT)) {
                flag = this.Twodarrinitopt1();
            }
            else {
                flag = this.AddError();
            }
        }
        else {
            if (this.doesContain(Selectionset.follow_TWODARRINITOPT)) {
                return true;
            }
            flag = this.AddError();
        }
        return flag;
    }
    
    private boolean AddError() {
        SyntaxAnalyser._error.add(SyntaxAnalyser._tokens.get(0));
        return false;
    }
    
    private boolean doesContain(final String[] arr) {
        final boolean doesContainValue = Arrays.stream(arr).anyMatch(x -> x.equals(SyntaxAnalyser._tokens.get(0).Value) || x.equals(SyntaxAnalyser._tokens.get(0).Class));
        return doesContainValue;
    }
}

