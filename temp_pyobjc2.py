from AppKit import NSWorkspace

workspace = NSWorkspace.sharedWorkspace()
print("Current Application Path:", workspace.frontmostApplication().bundleURL().path())

print("All Running Applications:")
for app in workspace.runningApplications():
    print("-", app.bundleURL().path())

print("Available Applications in /Applications:")
applications = workspace.urlsForApplicationsInDirectory_("/Applications")
for app_url in applications:
    print("-", app_url.path())
    

# """A minimal Cocoa application written in Python using the PyObjC bridge."""
# from Cocoa import NSObject, NSApplication, NSApp, NSWindow, NSButton, NSSound
# from PyObjCTools import AppHelper


