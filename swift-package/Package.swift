// swift-tools-version:5.2
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "{{name.lowercase}}",
    platforms: [
        .macOS(.v10_15)
    ],
    products: [
        .executable(name: "{{name.lowercase}}", targets: ["{{name.lowercase}}"]),
        .library(name: "{{name}}Lib", targets: ["{{name}}Lib"])
    ],
    targets: [
        .target(
            name: "{{name.lowercase}}",
            dependencies: ["{{name}}Lib"]
        ),
        .target(
            name: "{{name}}Lib"
        ),
        .testTarget(
            name: "{{name}}LibTests",
            dependencies: ["{{name}}Lib"]
        )
    ]
)
