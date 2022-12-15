import java.io.File;
public class FileInfo {
    public static void main(String[] args) {
        File f=new File("F:\\B-tech-2\\B-tech-2-1\\Labs\\JavaLab\\Experment-16\\Calculator");
        if(f.exists()){
            System.out.println("File status:"+f.exists());
            System.out.println("File reading state:"+f.canRead());
            System.out.println("file writing State"+f.canWrite());
            System.out.println("file lenght:"+f.length()+"byte");
        }else{
            System.out.println("file not found");
        }
    }
}
