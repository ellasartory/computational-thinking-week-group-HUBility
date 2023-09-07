import java.nio.file.{Files, Paths}
import scala.util.Try

object Main {
  def main(args: Array[String]): Unit = {
    val filePath = "data6.txt"

    // Check if the input file exists
    if (Files.exists(Paths.get(filePath))) {
      val lines = scala.io.Source.fromFile(filePath).getLines().toList
      val outputLines = lines.zipWithIndex.map {
        case (line, 0) => s"$line,Comments"
        case (line, _) =>
          val parts = line.split(",")
          if (parts.length < 9) line // skip invalid lines by accounting for 0-based indexing)
          else {
            val summary = parts(7)
            val evaluation = Try(parts(8).toFloat).getOrElse(0.0f) // To handle invalid float conversion
            val comments = (summary, evaluation) match {
              case ("super", e) if e >= 3 => "Excellent"
              case ("super", _) => "Good but inconsistent"
              case (_, e) if e >= 2 => "Promising"
              case _ => "Needs Improvement"
            }
            s"$line,$comments"
          }
      }

      // Write the outputLines to a new file
      Files.write(Paths.get("data7.txt"), outputLines.mkString("\n").getBytes)
    } else {
      println("Input file does not exist.")
    }
  }
}