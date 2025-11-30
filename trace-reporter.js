const fs = require('fs/promises');
const path = require('path');

const TRACE_TARGET_DIR = path.join(__dirname, 'qa_artifacts', 'traces');

const slug = (value) =>
  value.replace(/[\\/:<>|?*"\\s]+/g, '_').slice(0, 80) || 'trace';

class TraceReporter {
  async onTestEnd(test, result) {
    const traceAttachment = result.attachments?.find(
      (attachment) => attachment.name === 'trace' && attachment.path
    );
    if (!traceAttachment) return;

    await fs.mkdir(TRACE_TARGET_DIR, { recursive: true });

    const project = slug(test.projectName || 'project');
    const title = slug(test.title);
    const retry = result.retry ?? 0;
    const base = path.basename(traceAttachment.path, '.zip');
    const filename = `${project}-${title}-retry${retry}-${base}.zip`;
    const destination = path.join(TRACE_TARGET_DIR, filename);

    await fs.copyFile(traceAttachment.path, destination);
  }
}

module.exports = TraceReporter;
