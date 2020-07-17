import Foundation
import {{name}}Lib

do {
    try {{name}}().run(Array(CommandLine.arguments.dropFirst()))
} catch {
    print(error.localizedDescription)
}
