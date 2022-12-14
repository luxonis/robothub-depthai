import robothub_depthai


class ExampleApplication(robothub_depthai.RobotHubApplication):
    def on_start(self):
        for camera in self.hub_cameras:
            color = camera.create_camera('color', resolution='1080p', fps=30)

            # It will automatically create a stream and assign matching callback based on Component type
            camera.create_stream(component=color, unique_key=f'color_{camera.id}', name='Color stream')
